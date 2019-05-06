#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
from importlib import reload
import sys
sys.path.insert(0, '../database/')
reload(sys)
<<<<<<< Updated upstream
#import bdr
=======
import bdr
"""
>>>>>>> Stashed changes

import json




def get_restaurants():
	""" """
	restaurants = '''{"restaurants": 
		[
			{"id":1, "name":"Restaurant INSA", "status":"open", "eta":2500},
			{"id":2, "name":"Olivier", "status":"closed", "eta":2500},
			{"id":3, "name":"Grillon", "status":"open", "eta":2500},
			{"id":4, "name":"Prévert", "status":"open", "eta":2500},
			{"id":5, "name":"Le Pied du Saule", "status":"closed", "eta":2500}
		]
	}'''
	
	import mysql.connector

	mydb = mysql.connector.connect(
		host="localhost",
		user="root",
		passwd="toorTOOR2019!",
		database="main"
	)

	print(mydb)

	request = "select * from restaurant;"

	mycursor = mydb.cursor()
	mycursor.execute(request)
	
	myresult = mycursor.fetchall()

	restaurants = """{"restaurants": ["""
	for i, restaurant in enumerate(myresult):
		restaurants += """{{ "id":{}, "name":{}, "theme": {} ,"status":"closed", "eta":2500 }}""".format(restaurant[0], restaurant[1], restaurant[2])
		if i != len(myresult):
			restaurants += ","
	restaurants += """ ] } """

	return restaurants
	
	

def test():
	#Code Exemple
<<<<<<< Updated upstream
	#a = bdr.sgbd("../database/mydb.db") # metis
	#a.execute_script_from_file("../database/SQL_script_DB_Init.sql") # SQL_script_DB_Init
	#a.commit()
	#donnee = ("titi", )
	#results = a.execution("PRAGMA database_list;") #"SELECT * FROM Restaurant")
	#results = a.execution("attach database 'example.db' as another_db;")
	#a.print_all_results(results)
	#a.exit()
	pass
=======
	a = bdr.sgbd("../database/mydb.db") # metis
	a.execute_script_from_file("../database/SQL_script_DB_Init.sql") # SQL_script_DB_Init
	a.commit()
	donnee = ("titi", )
	results = a.execution("PRAGMA database_list;") #"SELECT * FROM Restaurant")
	results = a.execution("attach database 'example.db' as another_db;")
	a.print_all_results(results)
	a.exit()
>>>>>>> Stashed changes

#test()
