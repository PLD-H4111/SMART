#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import mysql.connector

from service_get_restaurants import get_restaurants
from service_get_restaurants_details import get_restaurants_details
from service_login_admin import login_admin
from service_create_restaurants_event import create_restaurants_event

import service5
import sensor_upload
import service_get_data_sensors
import service_get_sensor_list
import service_get_last_state_sensors
import service_upload_waiting_time


# TODO: verifier l'authentification pour les services sensibles
# TODO: injection SQL
# i.e user_data == None

# TODO: change date to datetime in json


class ActionServlet:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7291089",
            passwd="bbf4tfEUn1",
            database="sql7291089",
            use_pure=True
        )
        """self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toorTOOR2019!",
            database="main"
        )"""

    def fetch(self, user_data, input_data):
        """ """
        print("input data", input_data)
        print("action servlet:", input_data["action"])

        if "action" not in input_data:
            json_error = '''{
                "error": "there's no 'action' parameter in the parameters passed as input"
            }'''
            return user_data, json_error
        else:
            if input_data["action"] == "get-restaurants-list":
                return user_data, get_restaurants()


            elif input_data["action"] == "get-restaurant-details":
                if "restaurants" not in input_data:
                    json_error = '''{
                        "error": "there's no 'restaurants' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, get_restaurants_details(input_data["restaurants"], input_data["date"])


            elif input_data["action"] == "admin-login":
                if "login" not in input_data:
                    json_error = '''{
                        "error": "there's no 'login' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "password" not in input_data:
                    json_error = '''{
                        "error": "there's no 'password' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return login_admin(user_data, input_data["login"], input_data["password"])


            elif input_data["action"] == "create-restaurants-events":
                return user_data, create_restaurants_event(input_data["title"],
                                                           input_data["content"],
                                                           input_data["start"],
                                                           input_data["end"],
                                                           input_data["restaurants"])


            elif input_data["action"] == "get-restaurant-events":
                return user_data, service5.get_restaurant_events(self.mydb, input_data["restaurant"], input_data["date"])


            elif input_data["action"] == "get-all-restaurants-events":
                return user_data, service5.get_all_restaurants_events()


            elif input_data["action"] == "get-event-details":
                return user_data, service5.get_event_details(input_data["event"])


            elif input_data["action"] == "sensor-upload":
                return user_data, sensor_upload.sensor_upload(self.mydb, input_data["date_time"], input_data["sensor_id"], input_data["value"])


            elif input_data["action"] == "get-sensor-data":
                if "start_date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'start_date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "end_date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'end_date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, service_get_data_sensors.get_data_from_sensors(self.mydb, input_data["start_date"], input_data["end_date"])


            elif input_data["action"] == "get-sensor-list":
                return user_data, service_get_sensor_list.get_sensor_list(self.mydb)

            elif input_data["action"] == "get-last-state-sensors":
                if "end_date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'end_date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, service_get_last_state_sensors.get_last_state_sensors(self.mydb, input_data["end_date"])

            elif input_data["action"] == "upload-waiting-time":
                if "waiting_time" not in input_data:
                    json_error = '''{
                        "error": "there's no 'waiting_time' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "timestamp" not in input_data:
                    json_error = '''{
                        "error": "there's no 'timestamp' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "restaurant" not in input_data:
                    json_error = '''{
                        "error": "there's no 'restaurant' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, service_upload_waiting_time.upload_waiting_time(self.mydb, input_data["waiting_time"], input_data["timestamp"], input_data["restaurant"])


            else:
                json_error = '''{{
                    "error": "the action {} is not managed by the server"
                }}'''.format(input_data["action"])
                return user_data, json_error

