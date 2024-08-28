CREATE TABLE tigers (
    id  VARCHAR(10) NOT NULL PRIMARY KEY,
    sex VARCHAR(10) NOT NULL,
    generation VARCHAR(10) NOT NULL
);

CREATE TABLE species (
    species VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE locations (
    location VARCHAR(255) NOT NULL PRIMARY KEY
);

CREATE TABLE incidents (
    id VARCHAR(10) NOT NULL PRIMARY KEY,
    tiger VARCHAR(10) NOT NULL,
    month INTEGER NOT NULL,
    season VARCHAR(10) NOT NULL,
    year INTEGER NOT NULL,
    location VARCHAR(255) NOT NULL,
    prey_type CHAR(1) NOT NULL,
    prey_species VARCHAR(255) NOT NULL,
    prey_age VARCHAR(10) NOT NULL,
    prey_sex VARCHAR(10) NOT NULL,
    remarks TEXT,
    FOREIGN KEY fk_inc_tig(tiger) REFERENCES tigers(id),
    FOREIGN KEY fk_inc_loc(location) REFERENCES locations(location),
    FOREIGN KEY fk_inc_spec(prey_species) REFERENCES species(species)
);




