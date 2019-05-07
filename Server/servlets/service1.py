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




def get_restaurants0(database):
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
    
    request = "select * from Restaurant;"
    mycursor = database.cursor()
    
    mycursor.execute(request)
    myresult = mycursor.fetchall()

    restaurants = """{"restaurants": ["""
    for i, restaurant in enumerate(myresult):
        restaurants += """{{ "id": {},
                             "name": "{}",
                             "theme": "{}",
                             "status": "closed",
                             "eta": 2500 }}""".format(restaurant[0], restaurant[1], restaurant[2])
        if i != len(myresult)-1:
            restaurants += ","
    restaurants += """ ] } """

    return restaurants

    
    
    
    
    
    
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
    
    request = """SELECT PK_idRestaurant, name, theme, "1" AS status, w AS eta
    FROM Restaurant, RestaurantAvailabilities, WaitingTime,
	(SELECT o.waitingTime as w, name as nom

	FROM Restaurant, WaitingTime o LEFT JOIN WaitingTime b

		ON o.FK_restaurant = b.FK_restaurant AND o.date < b.date

	WHERE PK_idRestaurant = o.FK_restaurant

	AND b.date is NULL

    )o

    WHERE PK_idRestaurant = RestaurantAvailabilities.FK_restaurant

    AND nom = name
    AND PK_idRestaurant = WaitingTime.FK_restaurant

    AND RestaurantAvailabilities.date = date(NOW())

    AND openingTime < time(NOW())

    AND closingTime > time(NOW())
    UNION

    SELECT PK_idRestaurant, name, theme, "0" AS status, w AS eta
    FROM Restaurant, 

	    (SELECT o.waitingTime as w, name as nom

	    FROM Restaurant, WaitingTime o LEFT JOIN WaitingTime b

		    ON o.FK_restaurant = b.FK_restaurant AND o.date < b.date

	    WHERE PK_idRestaurant = o.FK_restaurant

	    AND b.date is NULL

        )o

    WHERE nom = name

    AND name NOT IN (
	    SELECT name FROM Restaurant, RestaurantAvailabilities 
	    
	    WHERE PK_idRestaurant = FK_restaurant

	    AND RestaurantAvailabilities.date = date(NOW())
	    
	    AND openingTime < time(NOW())
	    
	    AND closingTime > time(NOW())
	    )
    ;
    """
    mycursor = database.cursor()
    
    mycursor.execute(request)
    myresult = mycursor.fetchall()

    restaurants = """{"restaurants": ["""
    for i, restaurant in enumerate(myresult):
        restaurants += """{{ "id": {},
                             "name": "{}",
                             "theme": "{}",
                             "status": {},
                             "eta": {} }}""".format(restaurant[0], restaurant[1], restaurant[2], restaurant[3], restaurant[4])
        if i != len(myresult)-1:
            restaurants += ","
    restaurants += """ ] } """
    
    return restaurants

