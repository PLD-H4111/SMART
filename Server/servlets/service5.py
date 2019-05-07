#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def get_restaurant_event(database, restaurant_id, date):
    """ """
    
    request = "select * from Event where FK_idRestaurant = " + restaurant_id
    mycursor = database.cursor()    
    mycursor.execute(request)
    queryResult = mycursor.fetchone()
    
    if queryResult != None:   
        json_result = """{ "events": [""" 
        json_result += '''{{
            "name": "",
            "start": "",
            "end": "",
            "content": "",
            
        }}'''.format(queryResult[1], queryResult[2])
    else:
        json_result = '''{
            "error": "Events for this restaurant doesn't exist in the database."
        }'''
        
    json_result += """ ] } """
    return json_result;

def get_all_restaurants_news():
    """ """
    request = "select * from Event
    mycursor = database.cursor()    
    mycursor.execute(request)
    queryResult = mycursor.fetchone()
    
    if queryResult != None:    
        json_result = """{ "events": ["""
        
        
        json_result += '''{{
            "name": "",
            "start": "",
            "end": "" 
        }}'''.format(queryResult[1], queryResult[2])
    else:
        json_result = '''{
            "error": "Events doesn't exist in the database."
        }'''
        
    json_result += """ ] } """
    return json_result;


def get_event_details(event_id):
    """ """       
    request = "select * from Event where PK_idEvent = " + event_id
    mycursor = database.cursor()    
    mycursor.execute(request)
    queryResult = mycursor.fetchone()
    
    print(queryResult)
    
    json_result = ""
    if queryResult != None:    
        json_result = '''{{
            "name": "{}",
            "start": "{}",
            "end": "",
            "content": ""
        }}'''.format(queryResult[1], queryResult[2])
    else:
        json_result = '''{
            "error": "the event ID doesn't exist in the database."
        }'''
    return json_result;

  
