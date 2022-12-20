\echo --- taula cotxe
CREATE TABLE cotxe(
	matricula domini_matricula PRIMARY KEY,
	marca domini_marca NOT NULL,
	color domini_color NOT NULL,
	model VARCHAR (50) NOT NULL,
	dni_client domini_dni,
	CONSTRAINT dni_client_inexistent
		FOREIGN KEY (dni_client)
		REFERENCES client(dni)
			ON DELETE SET NULL
			ON UPDATE CASCADE
);
