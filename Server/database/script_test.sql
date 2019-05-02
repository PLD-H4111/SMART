DROP TABLE IF EXISTS scores;

CREATE TABLE IF NOT EXISTS scores(
id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
pseudo TEXT,
valeur INTEGER);

INSERT INTO scores(pseudo, valeur) VALUES ("toto", 1000);
INSERT INTO scores(pseudo, valeur) VALUES ("tata", 750);
INSERT INTO scores(pseudo, valeur) VALUES ("titi", 500);
INSERT INTO scores(pseudo, valeur) VALUES ("titi", 233);
