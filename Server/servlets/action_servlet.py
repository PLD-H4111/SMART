#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json

import service1
import service2


def fetch(input_data):
	""" """
	if "action" not in input_data:
		# pas la bonne structure de l'input data
		pass

	print("action servlet:", input_data["action"][0])
	
	if input_data["action"][0] == "get-restaurants-list":	
		return service1.get_restaurants()
	elif input_data["action"][0] == "get-restaurants-details":
		return service2.get_restaurant_details(restaurant_id)
	else:
		pass
	
	

