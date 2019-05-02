import sqlite3

class sgbd:
	def __init__(self, name):
		self.connexion = sqlite3.connect(name)
		self.cursor = self.connexion.cursor()
	def execute_script(self, script):
		self.cursor.executescript(script)
	def execute_script_from_file(self, filename):
		my_file = open(filename, "r")
		content = my_file.read()
		my_file.close()
		self.execute_script(content)
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
a.execute_script_from_file("script_test.sql")
a.commit()
donnee = ("titi", )
results = a.execution("SELECT valeur FROM scores WHERE pseudo = ?", donnee)
a.print_all_results(results)
a.exit()
