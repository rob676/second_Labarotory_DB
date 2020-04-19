import cx_Oracle

import chart_studio
chart_studio.tools.set_credentials_file(username='Kate_Hryhorenko', api_key='S6Cu2THhk1VIBPXEKZVf')
conn = cx_Oracle.connect("SYSTEM","2805052001","lockalhost/xe")
cur = conn.cursor()

cur.execute('''
SELECT
ROUND(AVG(coastline),3) AS coastline
, TRIM(region.region) AS region
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region.region;

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
layout = go.Layout(
    title='Coast of land in different regions',
    xaxis=dict(
        title='Region',
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    ),
    yaxis=dict(
        title='Cost per area',
        rangemode='nonnegative',
        autorange=True,
        titlefont=dict(
            family='Courier New, monospace',
            size=18,
            color='#7f7f7f'
        )
    )
)
fig = go.Figure(data=bar, layout=layout)


bar_coastline_url=py.plot(fig,filename='coast of land in different regions', auto_open=False)

cur.execute('''
SELECT
SUM(country.gdp) AS GDP
,TRIM(region.region)
FROM country
INNER JOIN region
ON country.region_id= region.region_id
GROUP BY region.region;
''')


rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)
pie = go.Figure(data=[go.Pie(labels=y, values=x )])
pie_gdp_url=py.plot(pie, filename='The sum of all the GDP of region realetive to the GDP of the Earth ',auto_open=False)

cur.execute('''   SELECT
round(SUM(net_migration),3) AS migrations
,TRIM(region.region)
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region.region;
''')

rows = cur.fetchall()
x = []
y = []
for row in rows:
    x.append(row[0])
    y.append(row[1])
print(x, y)

scatter = go.Figure([go.Scatter(x=y, y=x)])

scatter_migration_url=py.plot(scatter, filename = 'Level of migration above the regions', auto_open=False)

import re
import chart_studio.dashboard_objs as dashboard
def fileId_from_url(url):
    raw_fileId = re.findall("~[A-z.]+/[0-9]+", url)[0][1: ]
    return raw_fileId.replace('/', ':')

my_dboard = dashboard.Dashboard()

scatter_migration= fileId_from_url(scatter_migration_url)
pie_gdp= fileId_from_url(pie_gdp_url)
bar_coastline= fileId_from_url(bar_coastline_url)

box_1 = {
    'type': 'box',
    'boxType': 'plot',
    'fileId':bar_coastline,
    'title': 'coast of land in different regions'
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

py.dashboard_ops.upload(my_dboard, 'Dashboard')

conn.c
