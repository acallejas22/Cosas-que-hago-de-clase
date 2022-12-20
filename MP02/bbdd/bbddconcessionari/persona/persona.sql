\echo --- taula persona
CREATE TABLE persona(
	dni domini_dni PRIMARY KEY,
	nom VARCHAR (50) NOT NULL,
	cognoms VARCHAR (50) NOT NULL,
	adreca domini_adreca NOT NULL,
	datanaixement TIMESTAMP,
	edat domini_edat,
	email domini_email,
	CONSTRAINT email_ja_existent UNIQUE (email)
	
);
