import sqlite3

class sgbd:
    def __init__(self, name):
        self.connexion = sqlite3.connect(name)
        self.curseur = self.connexion.cursor()
    def execute_script(self, script):
        self.curseur.executescript(script)
    def execution(self, request, data):
        self.curseur.execute(request, data)
        return self.curseur.fetchall()
    def execution_print(self, request, data):
        self.curseur.execute(request, data)
        self.print_all_results()
    def commit(self):
        self.connexion.commit()
    def print_all_results(self):
        resultats = self.curseur.fetchall()
        for resultat in resultats:
            print(resultat)
    def print_all_results(self, resultats):
        for resultat in resultats:
            print(resultat)
    def exit(self):
        self.connexion.close()

#Code Exemple
a = sgbd("basededonnees.db")
a.execute_script("""

    DROP TABLE IF EXISTS scores;

    CREATE TABLE IF NOT EXISTS scores(
    id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
    pseudo TEXT,
    valeur INTEGER);
    
    INSERT INTO scores(pseudo, valeur) VALUES ("toto", 1000);
    INSERT INTO scores(pseudo, valeur) VALUES ("tata", 750);
    INSERT INTO scores(pseudo, valeur) VALUES ("titi", 500);
    INSERT INTO scores(pseudo, valeur) VALUES ("titi", 233);
""")
a.commit()
donnee = ("titi", )
resultats = a.execution("SELECT valeur FROM scores WHERE pseudo = ?", donnee)
a.print_all_results(resultats)
a.exit()
