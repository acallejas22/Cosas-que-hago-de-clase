\echo --- taula client
CREATE TABLE client (
	dni domini_dni PRIMARY KEY REFERENCES persona,
	nom_concessionari varchar(50),
	CONSTRAINT concessionari_inexistent
	FOREIGN KEY (nom_concessionari)
		ON DELETE SET NULL
		ON UPDATE CASCADE

);
