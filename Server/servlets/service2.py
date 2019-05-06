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
    
    restaurant_details = '''
    {{"restaurants": [
    {{
		"name": {},
        "theme": {},
        "status": "open",
        "schedule": "7/7 24/24",
        "throughput": "8",
        "eta": 15,
        "data": [
                {{"date": "08:35:30", "realtime": 5}},
                {{"date": "09:35:40", "realtime": 10}},
                {{"date": "10:35:50", "predicted": 20}},
                {{"date": "11:36:00", "predicted": 50}}
        ]
	}},
    {{		
        "name": "A",
        "theme": "A",
        "status": "open",
        "schedule": "7/7 24/24",
        "throughput": "8",
        "eta": 15,
        "data": [
                {{"date": "08:25:30", "realtime": 8}},
                {{"date": "09:25:40", "realtime": 20}},
                {{"date": "10:25:50", "predicted": 10}},
                {{"date": "11:26:00", "predicted": 42}}
        ]
	}},
    {{		
        "name": "B",
        "theme": "B",
        "status": "open",
        "schedule": "7/7 24/24",
        "throughput": "8",
        "eta": 15,
        "data": [
                {{"date": "08:15:36", "realtime": 40}},
                {{"date": "09:11:40", "realtime": 45}}
        ]
	}},
    {{		
        "name": "C",
        "theme": "C",
        "status": "open",
        "schedule": "7/7 24/24",
        "throughput": "8",
        "eta": 15,
        "data": [
                {{"date": "10:12:50", "predicted": 60}},
                {{"date": "11:16:20", "predicted": 80}}
        ]
	}}
    ]}}'''.format('"Zero"', '"Theme Zero"');
    return restaurant_details;


