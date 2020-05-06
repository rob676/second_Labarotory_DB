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
    round(AVG(population * gdp * services)) DESC;
    
SELECT
    SUM(gdp) AS gdp,
    region
FROM
   region left
    JOIN country ON region.region = country.region1
    LEFT JOIN gdp ON gdp.country_fk = country.country
GROUP BY
    region;
    
 SELECT
    round(SUM(net_migration), 3) AS "net migration",
    region
FROM
    region left
    JOIN country ON region.region = country.region1
    LEFT JOIN net_migration ON net_migration.country_fk = country.country
GROUP BY
    region
ORDER BY
    "net migration" DESC;