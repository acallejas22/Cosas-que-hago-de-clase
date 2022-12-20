CREATE DOMAIN domini_marca TEXT
	CHECK(VALUE IN('Audi', 'BMW', 'Frerrari', 'Mercedez-Benz')
);

CREATE DOMAIN domini_color VARCHAR(15)
	CHECK (VALUE IN('Negre', 'Vermell', 'Groc', 'Verd', 'Blau', 'Taronja', 'Daurat', 'Gris', 'Blanc')
);

CREATE DOMAIN domini_matricula VARCHAR(8)
	CHECK(VALUE LIKE '____ ___');

CREATE DOMAIN domini_edat SMALLINT
	CHECK(VALUE > 0 AND VALUE < 150);

CREATE DOMAIN domini_adreca TEXT
	CHECK (VALUE LIKE '__%, _%, _%, _%, ____, _%, _%');

CREATE DOMAIN domini_dni VARCHAR(9)
	CHECK (VALUE LIKE '_________');

CREATE DOMAIN domini_email TEXT
CHECK (VALUE LIKE '%_@%_.%_');

CREATE DOMAIN domini_codipostal TEXT
	CHECK(VALUE LIKE '_______');
