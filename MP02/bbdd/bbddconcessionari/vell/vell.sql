\echo -- taula vell
CREATE TABLE vell(
	matricula domini_matricula PRIMARY KEY REFERENCES cotxe
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	km numeric (10, 2)
);

