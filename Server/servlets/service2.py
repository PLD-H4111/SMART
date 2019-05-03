#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json



def get_restaurant_details(restaurant_id, date):
    """ """
    restaurant_name = {}
    restaurant_name[1] = '"Restaurant INSA"'
    restaurant_name[2] = '"Olivier"'
    restaurant_name[3] = '"Grillon"'
    restaurant_name[4] = '"Prévert"'
    restaurant_name[5] = '"Le Pied du Saule"'
    
    restaurant_theme = {}
    restaurant_theme[1] = '"La bonne bouffe du Beurk"'
    restaurant_theme[2] = '"Les bonnes pizzas surgelées"'
    restaurant_theme[3] = '"Les bonnes cotelettes trop cuites"'
    restaurant_theme[4] = '"Le fast food de la déprime"'
    restaurant_theme[5] = '"Rendez-vous du 3ème âge"'
    
    restaurant_details = '''{{
		"name": {},
        "theme": {},
        "status": "open",
        "schedule": "7/7 24/24",
        "throughput": "8p/min",
        "eta": 15,
        "data": [
                {{"date": "08:15:30", "realtime": 5}},
                {{"date": "09:15:40", "realtime": 10}},
                {{"date": "10:15:50", "predicted": 20}},
                {{"date": "11:16:00", "predicted": 50}}
        ]
	}}'''.format(restaurant_name[int(restaurant_id)], restaurant_theme[int(restaurant_id)])
    return restaurant_details


