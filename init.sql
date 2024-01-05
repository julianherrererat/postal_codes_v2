USE codigos_postales;

CREATE TABLE coordenadas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    latitud FLOAT,
    longuitud FLOAT
);


CREATE TABLE codigos_postales (
    id INT AUTO_INCREMENT PRIMARY KEY,
    postcode VARCHAR(20),
    quality INT,
    eastings INT,
    northings INT,
    country VARCHAR(50),
    nhs_ha VARCHAR(50),
    longitude DECIMAL(10, 6),
    latitude DECIMAL(10, 6),
    european_electoral_region VARCHAR(50),
    primary_care_trust VARCHAR(50),
    region VARCHAR(50),
    lsoa VARCHAR(50),
    msoa VARCHAR(50),
    incode VARCHAR(10),
    outcode VARCHAR(10),
    parliamentary_constituency VARCHAR(50),
    admin_district VARCHAR(50),
    parish VARCHAR(50),
    admin_county VARCHAR(50),
    date_of_introduction VARCHAR(20),
    admin_ward VARCHAR(50),
    ced VARCHAR(50),
    ccg VARCHAR(50),
    nuts VARCHAR(50),
    pfa VARCHAR(50),
    distance DECIMAL(10, 8),
    admin_district_code VARCHAR(20),
    admin_county_code VARCHAR(20),
    admin_ward_code VARCHAR(20),
    parish_code VARCHAR(20),
    parliamentary_constituency_code VARCHAR(20),
    ccg_code VARCHAR(20),
    ccg_id VARCHAR(20),
    ced_code VARCHAR(20),
    nuts_code VARCHAR(20),
    lsoa_code VARCHAR(20),
    msoa_code VARCHAR(20),
    lau2_code VARCHAR(20),
    pfa_code VARCHAR(20),
    fk_id INT
    
);


CREATE TABLE errores (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_coordenada VARCHAR(50),  
    latitud DECIMAL(10,6),
    longitud DECIMAL(10,6), 
    observaciones TEXT
);

CREATE TABLE maxid (
    id INT 
);