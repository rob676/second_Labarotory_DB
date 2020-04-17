CREATE TABLE country(
country varchar(60) NOT NULL
,coastline float NULL
,net_migration float NULL
,GDP float NULL
,CONSTRAINT country_pk PRIMARY KEY (country)
);


CREATE TABLE region(
region varchar(70) NOT NULL
,country varchar(60) NOT NULL
, CONSTRAINT region_pk 
PRIMARY KEY (region)
,CONSTRAINT country_fk 
FOREIGN KEY (country)
REFERENCES country (country)
);