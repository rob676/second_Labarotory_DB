import cx_Oracle

conn = cx_Oracle.connect("SYSTEM","2805052001","lockalhost/xe")
cur = conn.cursor()

cur.execute('''
SELECT
ROUND(AVG(coastline),3) AS coastline
, TRIM(region.region) AS region
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region.region
ORDER BY  coastline DESC;

''')

rows = cur.fetchall()
print(rows)

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
print(rows)

cur.execute('''    SELECT
SUM(net_migration) AS migrations
,TRIM(region.region)
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region.region
ORDER BY  migrations DESC;
''')

rows = cur.fetchall()
print(rows)

conn.close()
