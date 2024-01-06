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
    codes_admin_district	VARCHAR(20),
    codes_admin_county VARCHAR(20),
    codes_admin_ward	VARCHAR(20),
    codes_parish	VARCHAR(20),
    codes_parliamentary_constituency	VARCHAR(20),
    codes_ccg VARCHAR(20),
    codes_ccg_id	VARCHAR(20),
    codes_ced VARCHAR(20),
    codes_nuts VARCHAR(20),
    codes_lsoa VARCHAR(20),
    codes_msoa VARCHAR(20),
    codes_lau2 VARCHAR(20),
    codes_pfa VARCHAR(20),
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