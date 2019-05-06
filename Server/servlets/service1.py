#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""
from importlib import reload
import sys
sys.path.insert(0, '../database/')
reload(sys)
#import bdr
=======
import bdr
"""

import json




def get_restaurants(database):
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
    
    request = "select * from restaurant;"
    mycursor = database.cursor()
    
    mycursor.execute(request)
    myresult = mycursor.fetchall()

    restaurants = """{"restaurants": ["""
    for i, restaurant in enumerate(myresult):
        restaurants += """{{ "id":{}, "name":"{}", "theme": "{}" ,"status":"closed", "eta":2500 }}""".format(restaurant[0], restaurant[1], restaurant[2])
        if i != len(myresult)-1:
            restaurants += ","
    restaurants += """ ] } """

    return restaurants

