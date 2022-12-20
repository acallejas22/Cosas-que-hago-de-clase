\echo --- taula clienttelefon
CREAT ETABLE clienttelefon (
	dni domini_dni PRIMARY KEY REFERENCES persona
		ON DELETE CASCADE
		ON UPDATE CASCADE,
	telefon VARCHAR(20) NOT NULL,
	UNICQUE (dni, telefon)
);
