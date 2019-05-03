#!/usr/bin/python3
# -*- coding: utf-8 -*-


from importlib import reload
import sys
sys.path.insert(0, '../database/')
reload(sys)
import bdr

import json




def get_restaurants():
	""" """
	restaurants = '''{"restaurants": 
		[
			{"id":1, "name":"marche ou crêpe", "status":"open", "eta":2500},
			{"id":2, "name":"nothing Toulouse", "status":"closed", "eta":2500},
			{"id":3, "name":"Kim aime me suive", "status":"open", "eta":2500},
			{"id":4, "name":"vingt heures vin", "status":"open", "eta":2500},
			{"id":5, "name":"les friands disent...", "status":"closed", "eta":2500},
			{"id":6, "name":"Dupont avec un thé", "status":"open", "eta":2500},
			{"id":7, "name":"Chez Riz", "status":"open", "eta":2500}
		]
	}'''
	return restaurants
	
	

def test():
	#Code Exemple
	a = bdr.sgbd("../database/mydb.db") # metis
	a.execute_script_from_file("../database/SQL_script_DB_Init.sql") # SQL_script_DB_Init
	a.commit()
	donnee = ("titi", )
	results = a.execution("PRAGMA database_list;") #"SELECT * FROM Restaurant")
	results = a.execution("attach database 'example.db' as another_db;")
	a.print_all_results(results)
	a.exit()

test()
