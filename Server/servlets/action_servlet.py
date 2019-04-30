#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json

import service1



def fetch(input_data):
	""" """
	if "action" not in input_data:
		# pas la bonne structure de l'input data
		pass

	if input_data["action"][0] == "get-restaurants-list":
		print("action servlet:", input_data["action"][0])
		return service1.get_restaurants()
	elif input_data["action"][0] == "other":
		pass
	else:
		pass
	
	

