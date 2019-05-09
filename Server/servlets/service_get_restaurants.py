#!/usr/bin/python3
# -*- coding: utf-8 -*-


from datetime import date, datetime, timedelta
import json
import dao



'''{"restaurants":
        [
            {"id":1, "name":"Restaurant INSA", "status":"open", "eta":2500},
            {"id":2, "name":"Olivier", "status":"closed", "eta":2500},
            {"id":3, "name":"Grillon", "status":"open", "eta":2500},
            {"id":4, "name":"Prévert", "status":"open", "eta":2500},
            {"id":5, "name":"Le Pied du Saule", "status":"closed", "eta":2500}
        ]
    }'''


def get_restaurants(database):
    """ """
    json_result = """{"restaurants": ["""

    today_date = date.today().strftime("%Y-%m-%d")
    now = datetime.now()

    restaurants = dao.select_all_restaurants(database)
    for i, restaurant in enumerate(restaurants):
        id = restaurant[0]
        name = restaurant[1]
        theme = restaurant[2]
        waitingTime = ""
        availability = ""

        waiting_time_tuple = dao.select_last_waiting_time(database, id)
        waitingTime = extract_waiting_time(waiting_time_tuple)

        availability_tuple = dao.select_actual_restaurant_availability(database, id)
        if availability_tuple != None:
            availability = 1
        else:
            availability = 0

        json_result += """{{ "id": {},
                             "name": "{}",
                             "theme": "{}",
                             "status": {},
                             "eta": "{}" }}""".format(id, name, theme, availability, waitingTime)
        if i != len(restaurants)-1:
            json_result += ",\n"
    json_result += """ ] } """
    return json_result


def extract_waiting_time(waiting_time_tuple):
    """ extract waiting time from a tuple of the WaitingTime table """
    waitingTime = ""
    if waiting_time_tuple != None:
        a = waiting_time_tuple[2]
        b = datetime.now()
        c = b - a
        delta = timedelta(0, 600, 0) # 10 minutes
        if b >= a and c < delta:
            waitingTime = str(waiting_time_tuple[1])
        else:
            waitingTime = "N/A"
    else:
        waitingTime = "N/A"
    return waitingTime


