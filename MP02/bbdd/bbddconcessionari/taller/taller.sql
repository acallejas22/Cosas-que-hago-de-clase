\echo --- taula taller
CREATE TABLE taller (
	nom VARCHAR(50) PRIMARY KEY,
	nom_concessionari VARCHAR(50),
	CONSTRAINT concessionari_inexistent
	FOREIGN KEY (nom_concessionari)
	REFERENCES concessionari (nom)
	ON DELETE SET NULL
	ON UPDATE CASCADE	
);
