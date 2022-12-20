\echo --- taula repara
CREATE TABLE repara(
	dni_mecanic domini_dni NOT NULL REFERENCES mecanic
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	matricula domini_matricula NOT NULL REFERENCES cotxe
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	numhores DECIMAL (4, 2) DEFAULT 1.00,
	data TIMESTAMP NOT NULL

);

