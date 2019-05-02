import sqlite3

class sgbd:
	def __init__(self, name):
		self.connexion = sqlite3.connect(name)
		self.cursor = self.connexion.cursor()
	def execute_script(self, script):
		self.cursor.executescript(script)
	def execution(self, request, data):
		self.cursor.execute(request, data)
		return self.cursor.fetchall()
	def execution_print(self, request, data):
		self.cursor.execute(request, data)
		self.print_all_results()
	def commit(self):
		self.connexion.commit()
	def print_all_results(self):
		results = self.cursor.fetchall()
		for result in results:
			print(result)
	def print_all_results(self, results):
		for result in results:
			print(result)
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
results = a.execution("SELECT valeur FROM scores WHERE pseudo = ?", donnee)
a.print_all_results(results)
a.exit()
