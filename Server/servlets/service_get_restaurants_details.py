#!/usr/bin/python3
# -*- coding: utf-8 -*-


from datetime import date, datetime, timedelta
import json
import dao


# TODO: change date to time in json data
# TODO: changer le format horaires dans json result



def get_restaurants_details(restaurants_ids, date_time):
    """ get the details of all the restaurants """
    date = date_time[:10]
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
        waitingTime = extract_waiting_time(waiting_time_tuple)

        availability_tuple = dao.select_actual_restaurant_availability(id)
        if availability_tuple != None:
            availability = 1
        else:
            availability = 0

        availabilities_tuples = dao.select_restaurant_availabilities(restaurant_id, date)
        if availabilities_tuples != None:
            for tuple in availabilities_tuples:
                schedule.append("{}h{}-{}h{}".format(str(tuple[2].seconds//3600).zfill(2),
                                             str(tuple[2].seconds%60).zfill(2),
                                             str(tuple[3].seconds//3600).zfill(2),
                                             str(tuple[3].seconds%60).zfill(2)))
        else:
            pass

        waiting_time_tuples = dao.select_waiting_times(restaurant_id, date)
        if waiting_time_tuples != None:
            for tuple in waiting_time_tuples:
                data.append({"date": tuple[2].strftime("%H:%M:%S"),
                             "realtime": tuple[1]})
        else:
            pass

        schedule = '["' + '", "'.join(schedule) + '"]'

        json_result = '''{{
            "id": {},
            "name": "{}",
            "theme": "{}",
            "status": {},
            "schedule": {},
            "throughput": "8p/min",
            "eta": "{}",
            "data": {}
        }}'''.format(id, name, theme, availability, schedule, waitingTime, json.dumps(data))
        return json_result
    else:
        json_error = '''{
            "error": "the restaurant ID doesn't exist in the database."
        }'''
        return json_error




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


