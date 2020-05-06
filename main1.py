import cx_Oracle


username = "SYSTEM"
password = "2805052001"
database = "T/xe"

try:
    connection = cx_Oracle.connect(username, password, database)
except cx_Oracle.DatabaseError as exception:
    print('Failed to connect to %s\n', database)
    print(exception)
    exit(1)
import chart_studio
chart_studio.tools.set_credentials_file(username='Kate_Hryhorenko', api_key='S6Cu2THhk1VIBPXEKZVf')

cur = connection.cursor()

cur.execute('''
SELECT
    round(AVG(population * gdp * services)) AS "money of service industry",
    region
FROM
    region left
    JOIN country ON region.region = country.region1
    LEFT JOIN gdp ON gdp.country_fk = country.country
    LEFT JOIN pop_destiny ON pop_destiny.country_fk = country.country
    LEFT JOIN country_type ON country_type.country_fk = country.country
GROUP BY
    region
ORDER BY
    round(AVG(population * gdp * services)) DESC
''')
rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

import plotly.graph_objects as go
import chart_studio.plotly as py
bar = [go.Bar(x=y, y=x)]

fig = go.Figure(data=bar)


bar_money_url=py.plot(fig,filename='Money of service industry.7', auto_open=False)

cur.execute('''
SELECT
    SUM(gdp) AS gdp,
    region
FROM
    region left
    JOIN country ON region.region = country.region1
    LEFT JOIN gdp ON gdp.country_fk = country.country
GROUP BY
    region
''')


rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
pie = go.Figure(data=[go.Pie(labels=y, values=x )])
pie_gdp_url=py.plot(pie, filename='The sum of all the GDP of region realetive to the GDP of the Earth.',auto_open=False)

cur.execute(''' SELECT
    round(SUM(net_migration), 3) AS "net migration",
    region
FROM
    region left
    JOIN country ON region.region = country.region1
    LEFT JOIN net_migration ON net_migration.country_fk = country.country 
GROUP BY
    region
ORDER BY
    "net migration" DESC
''')

rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

scatter = go.Figure([go.Scatter(x=y, y=x)])

scatter_migration_url=py.plot(scatter, filename = 'Level of migration above the regions.', auto_open=False)

import re
import chart_studio.dashboard_objs as dashboard
def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

my_dboard = dashboard.Dashboard()

scatter_migration= fileId_from_url(scatter_migration_url)
pie_gdp= fileId_from_url(pie_gdp_url)
bar_coastline= fileId_from_url(bar_money_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':bar_coastline,
    'title': 'Money of service industry'
}

box_2 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':pie_gdp,
    'title': 'The sum of all the GDP of region realetive to the GDP of the Earth '
}

box_3 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':scatter_migration ,
    'title': 'Level of migration above the regions'
}

my_dboard.insert(box_1)
my_dboard.insert(box_2, 'below', 1)
my_dboard.insert(box_3, 'left', 2)

py.dashboard_ops.upload(my_dboard, 'Dashboard.')

connection.commit()
cur.close()
connection.close()
