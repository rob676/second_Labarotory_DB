CREATE TABLE country(
country varchar(128) NOT NULL
,region_id number(6) NOT NULL
,coastline number(38,2) NULL
,net_migration number(38,2) NULL
,GDP number(38,2) NULL
,CONSTRAINT country_pk PRIMARY KEY (country)
,CONSTRAINT country_fk FOREIGN KEY (region_id) REFERENCES region (region_id)
);


CREATE TABLE region(
region varchar2(128) NOT NULL
,region_id number(6) NOT NULL
, CONSTRAINT region_pk PRIMARY KEY (region_id)
);