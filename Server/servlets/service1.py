#!/usr/bin/python3
# -*- coding: utf-8 -*-


from importlib import reload
import sys
sys.path.insert(0, '../database/')
reload(sys)
#import bdr

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
	return restaurants
	
	

def test():
	#Code Exemple
	#a = bdr.sgbd("../database/mydb.db") # metis
	#a.execute_script_from_file("../database/SQL_script_DB_Init.sql") # SQL_script_DB_Init
	#a.commit()
	#donnee = ("titi", )
	#results = a.execution("PRAGMA database_list;") #"SELECT * FROM Restaurant")
	#results = a.execution("attach database 'example.db' as another_db;")
	#a.print_all_results(results)
	#a.exit()
	pass

#test()
