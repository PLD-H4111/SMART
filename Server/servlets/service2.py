#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json



def get_restaurants_details(database, restaurants_ids, date):
    """ """
    json_result = """{ "restaurants": ["""
    for i, restaurant_id in enumerate(restaurants_ids):
        json_result += get_restaurant_details(database, restaurant_id, date)
        if i != len(restaurants_ids)-1:
            json_result += ", "
    json_result += """ ] } """
    return json_result


def get_restaurant_details(database, restaurant_id, date):
    """ """
    request = "select * from Restaurant where PK_idRestaurant = " + str(restaurant_id)
    mycursor = database.cursor()
    
    mycursor.execute(request)
    queryResult = mycursor.fetchone()
    
    print(queryResult)
    
    json_result = ""
    if queryResult != None:    
        json_result = '''{{
            "name": "{}",
            "theme": "{}",
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
        }}'''.format(queryResult[1], queryResult[2])
    else:
        json_result = '''{
            "error": "the restaurant ID doesn't exist in the database."
        }'''
    return json_result

