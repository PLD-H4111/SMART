#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def get_restaurant_event(database, restaurant_id, date):
    """ """
    
    request = "select name, eventDescription, beginningDate, endingDate from Event where FK_Restaurant = " + restaurant_id
    mycursor = database.cursor()    
    mycursor.execute(request)
    result = mycursor.fetchall()
    
    if result != None:
        json_result = """{ "events": ["""
        for index in range(len(result)):
            json_result += '''{{
                "name": "{}",
                "content": "{}",
                "start": "{}",
                "end": "{}"
            }}{}'''.format(result[index][0],
                           result[index][1],
                           result[index][2],
                           result[index][3],
                           "" if index == len(result)-1 else ",")
        json_result += """ ] } """
    else:
        json_result = '''{
            "error": "Events for this restaurant doesn't exist in the database."
        }'''
        
    return json_result;

def get_all_restaurants_events(database):
    """ """
    request = "select PK_idEvent, Event.name, beginningDate, endingDate, Restaurant.name from Event, Restaurant where Restaurant.PK_idRestaurant = Event.FK_Restaurant"
    mycursor = database.cursor()    
    mycursor.execute(request)
    result = mycursor.fetchall()
    
    if result != None:
        json_result = """{ "events": ["""
        for index in range(len(result)):
            json_result += '''{{
                "id": {},
                "name": "{}",
                "start": "{}",
                "end": "{}",
                "restaurant": "{}"
            }}{}'''.format(result[index][0],
                           result[index][1],
                           result[index][2],
                           result[index][3],
                           result[index][4],
                           "" if index == len(result)-1 else ",")
        json_result += """ ] } """
    else:
        json_result = '''{
            "error": "Events doesn't exist in the database."
        }'''
    return json_result;


def get_event_details(database, event_id):
    """ """       
    request = "select Event.name, eventDescription, beginningDate, endingDate, Restaurant.name from Event, Restaurant where Restaurant.PK_idRestaurant = Event.FK_Restaurant and PK_idEvent = " + event_id
    mycursor = database.cursor()    
    mycursor.execute(request)
    result = mycursor.fetchall()

    json_result = ""
    if result != None:
        json_result = '''{{ "event": {{
            "name": "{}",
            "content": "{}",
            "start": "{}",
            "end": "{}",
            "restaurants": ['''.format(result[0][0], result[0][1], result[0][2], result[0][3])
        for index in range(len(result)):
            json_result += '''"{}"{} '''.format(result[index][4], "" if index == len(result)-1 else ",")
        json_result += '''] }}'''
    else:
        json_result = '''{
            "error": "the event ID doesn't exist in the database."
        }'''
    return json_result;

  
