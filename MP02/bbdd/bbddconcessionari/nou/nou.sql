\echo --- taula nou
CREATE TABLE nou(
	matricula domini_matricula PRIMARY KEY REFERENCES cotxe
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	numerounitat SMALLINT DEFAILT 1
);
