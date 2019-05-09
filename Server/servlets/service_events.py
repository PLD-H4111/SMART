#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json
import dao

def get_restaurant_events(database, restaurant_id, date):
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
    result = dao.select_restaurants_events(database)

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
    result = dao.select_event_details(database, event_id)

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







def get_restaurant_event0s(restaurant_id, date):
    """ """
    result = dao.select_restaurant_events(restaurant_id, date)

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
