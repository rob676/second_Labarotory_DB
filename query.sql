SELECT
ROUND(AVG(coastline),3) AS coastline
, TRIM(region) AS region
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region
ORDER BY  coastline DESC;


SELECT
SUM(country.gdp) AS GDP
,TRIM(region.region)
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region;

SELECT
SUM(net_migration) AS migrations
,TRIM(region)
FROM country
INNER JOIN region
ON country.region_id= region.region_id 
GROUP BY region
ORDER BY  migrations DESC;






                     
