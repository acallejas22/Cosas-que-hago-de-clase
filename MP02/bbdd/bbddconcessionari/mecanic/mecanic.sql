\echo --- taula mecanic
CREATE TABLE mecanic(
	dni domini_dni PRIMARY KEY REFERENCES persona,
	salari REAL DEFAULT 1100.00 CHECK (salari > 0),
	datacontractacio TIMESTAMP NOT NULL,
	nom_taller VARCHAR (50) REFERENCES taller
		ON DELETE SET NULL
		ON UPDATE CASCADE

);
