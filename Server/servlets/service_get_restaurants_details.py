#!/usr/bin/python3
# -*- coding: utf-8 -*-


from importlib import reload
import sys
sys.path.insert(0, './database/')
reload(sys)

from datetime import date, datetime, timedelta
import json
import dao


# TODO: change date to time in json data



def get_restaurants_details(restaurants_ids, date):
    """ get the details of all the restaurants """
    json_result = """{ "restaurants": ["""
    for i, restaurant_id in enumerate(restaurants_ids):
        json_result += get_restaurant_details(restaurant_id, date)
        if i != len(restaurants_ids)-1:
            json_result += ", "
    json_result += """ ] } """
    return json_result
    
    
def get_restaurant_details(restaurant_id, date):
    """ get the details of a single restaurant """
    restaurant = dao.select_restaurant(restaurant_id)
    if restaurant != None:
        id = restaurant[0]
        name = restaurant[1]
        theme = restaurant[2]
        status = 0
        schedule = []
        waitingTime = ""
        data = []
        
        
        waiting_time_tuple = dao.select_last_waiting_time(id)
        availability_tuple = dao.select_actual_restaurant_availability(id)
        
        waitingTime = extract_waiting_time(waiting_time_tuple)
        
        if availability_tuple != None:
            availability = 1
        else:
            availability = 0
        
        json_result = '''{{
            "id": {},
            "name": "{}",
            "theme": "{}",
            "status": {},
            "schedule": ["12h-14h", "18h-20h"],
            "throughput": "8p/min",
            "eta": "{}",
            "data": [
                    {{"date": "08:15:30", "realtime": 5}},
                    {{"date": "09:15:40", "realtime": 10}},
                    {{"date": "10:15:50", "predicted": 20}},
                    {{"date": "11:16:00", "predicted": 50}}
            ]
        }}'''.format(id, name, theme, availability, waitingTime)
        return json_result
    else:
        json_error = '''{
            "error": "the restaurant ID doesn't exist in the database."
        }'''
        return json_error

    

    
    
    
    
    
    
    
    
def get_restaurant_details0(database, restaurant_id, date):
    """ """

    request = "select * from Restaurant where PK_idRestaurant = " + str(restaurant_id)
    mycursor = database.cursor()
    
    mycursor.execute(request)
    queryResult = mycursor.fetchone()
    
    json_result = ""
    if queryResult != None:    
        json_result = '''{{
            "name": "{}",
            "theme": "{}",
            "status": "open",
            "schedule": ["12h-14h", "18h-20h"],
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

    
    
def extract_waiting_time(waiting_time_tuple):
    """ extract waiting time from a tuple of the WaitingTime table """
    waitingTime = ""
    if waiting_time_tuple != None:
        #print("WTT 196", waiting_time_tuple)
        #print(waiting_time_tuple[2])
        a = waiting_time_tuple[2]
        b = datetime.now()
        #b = datetime(2019,5,2,12,10)
        c = b - a
        delta = timedelta(0, 600, 0) # 10 minutes
        if b >= a and c < delta:
            waitingTime = str(waiting_time_tuple[1])
        else:
            waitingTime = "N/A"
    else:
        waitingTime = "N/A"
    return waitingTime
    
    