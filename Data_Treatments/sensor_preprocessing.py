#!/bin/python3

import datetime
from datetime import date
from random import *
import json
import http_methods

distances_max = {"8": {"4": 800}}
IR_delta = datetime.timedelta(days=0,seconds=10)

def get_sensors_per_restaurant_from_database():
    params = {"action": "get-sensor-list"}
    return json.loads(http_methods.send_data(params))["sensors_per_restaurant"]

def get_data_from_database(start_date, end_date):
    params = {}
    params["action"] = "get-sensor-data"
    params["start_date"] = str(start_date)
    params["end_date"] = str(end_date)
    data = json.loads(http_methods.send_data(params))
    for restaurant_id, restaurant in data["data_per_restaurant"].items():
        for position, measures in restaurant.items():
            for measure in measures:
                measure["datetime"] = datetime.datetime.strptime(measure["datetime"], '%Y-%m-%d %H:%M:%S')

    return data["data_per_restaurant"]

def get_last_state_from_database(end_date):
    params = {}
    params["action"] = "get-last-state-sensors"
    params["end_date"] = str(end_date)
    data = json.loads(http_methods.send_data(params))
    for restaurant_id, restaurant in data["last_state_sensors"].items():
        for position, measure in restaurant.items():
                measure["datetime"] = datetime.datetime.strptime(measure["datetime"], '%Y-%m-%d %H:%M:%S')

    return data["last_state_sensors"]

def get_sensors_state_per_restaurant():
    sensors_per_restaurant = get_sensors_per_restaurant_from_database()

    start_date = datetime.datetime.now() - datetime.timedelta(days=0,seconds=30)
    end_date = start_date + datetime.timedelta(days=0,seconds=20)

    data = get_data_from_database(start_date, end_date)
    sensor_last_real_states = get_last_state_from_database(start_date)

    sensor_states = {}
    for restaurant_id, restaurant in sensors_per_restaurant.items():

        sensor_states[restaurant_id] = {}
        for sensor_type, positions in restaurant.items():
                sensor_states[restaurant_id][sensor_type] = {}
                for position in positions:
                    position = str(position)

                    if restaurant_id in data and position in data[restaurant_id]: #Data available
                        if sensor_type == "Ultrason":
                            total = 0
                            for measure in data[restaurant_id][position]:
                                total += int(measure["value"])
                            avg = total/len(data[restaurant_id][position])
                            sensor_states[restaurant_id][sensor_type][position] = (distances_max[restaurant_id][position] - avg)/distances_max[restaurant_id][position]
                        elif sensor_type == "Infrarouge":
                            if restaurant_id in sensor_last_real_states and position in sensor_last_real_states[restaurant_id]: #Add last state before start_date
                                data[restaurant_id][position].append(sensor_last_real_states[restaurant_id][position])

                            transitions = sorted(data[restaurant_id][position], key=lambda k: k["datetime"], reverse=True)
                            nb_transitions = len(transitions)
                            if nb_transitions > 1:
                                if end_date - transitions[0]["datetime"] >= IR_delta:
                                    sensor_states[restaurant_id][sensor_type][position] = transitions[0]["value"]
                                else:
                                    found = False
                                    for i in range(nb_transitions-1):
                                        diff = transitions[i]["datetime"] - transitions[i+1]["datetime"]
                                        if diff >= IR_delta:
                                            sensor_states[restaurant_id][sensor_type][position] = transitions[i+1]["value"]
                                            found = True
                                            break

                                    if found == False:
                                        sensor_states[restaurant_id][sensor_type][position] = -1 # Too noisy
                            elif nb_transitions == 1:
                                sensor_states[restaurant_id][sensor_type][position] = transitions[0]["value"] #Last state

                    else:
                        if restaurant_id in sensor_last_real_states and position in sensor_last_real_states[restaurant_id]:
                            sensor_states[restaurant_id][sensor_type][position] = sensor_last_real_states[restaurant_id][position]["value"]

    return sensor_states
