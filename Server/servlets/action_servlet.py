#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import mysql.connector

from service_get_restaurants import get_restaurants
from service_get_restaurants_details import get_restaurants_details
from service_login_admin import login_admin
from service_create_restaurants_event import create_restaurants_event

import service_events
import sensor_upload
import service_get_data_sensors
import service_get_sensor_list
import service_get_last_state_sensors
import service_upload_waiting_time



class ActionServlet:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7291089",
            passwd="bbf4tfEUn1",
            database="sql7291089",
            use_pure=True
        )

    def fetch(self, user_data, input_data):
        """ fetchs the parameters in input_data and call the right service to manage the request """

        if "action" not in input_data:
            json_error = '''{
                "error": "there's no 'action' parameter in the parameters passed as input"
            }'''
            return user_data, json_error
        else:
            # ----------------------- GET RESTAURANTS LIST -------------------
            if input_data["action"] == "get-restaurants-list":
                return user_data, get_restaurants(self.mydb)

            # ----------------------- GET RESTAURANT DETAILS -----------------
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
                    return user_data, get_restaurants_details(self.mydb, input_data["restaurants"], input_data["date"])

            # ----------------------- ADMIN LOGIN ----------------------------
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
                    return login_admin(self.mydb, user_data, input_data["login"], input_data["password"])

            # --------------------- CREATE RESTAURANTS EVENTS ----------------
            elif input_data["action"] == "create-restaurants-events":
                if user_data == None: # not logged in
                    json_error = '''{
                        "error": "You must log in as an administrator to request this service"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, create_restaurants_event(self.mydb, 
                                                               input_data["title"],
                                                               input_data["content"],
                                                               input_data["start"],
                                                               input_data["end"],
                                                               input_data["restaurants"])

            # ----------------------- GET RESTAURANTS EVENTS -----------------
            elif input_data["action"] == "get-restaurant-events":
                return user_data, service_events.get_restaurant_events(self.mydb, input_data["restaurant"], input_data["date"])

            # -------------------- GET ALL RESTAURANTS EVENTS ----------------
            elif input_data["action"] == "get-all-restaurants-events":
                return user_data, service_events.get_all_restaurants_events(self.mydb)

            # ----------------------- GET EVENT DETAILS ----------------------
            elif input_data["action"] == "get-event-details":
                return user_data, service_events.get_event_details(self.mydb, input_data["event"])

            # ----------------------- SENSOR UPLOAD --------------------------
            elif input_data["action"] == "sensor-upload":
                return user_data, sensor_upload.sensor_upload(self.mydb, input_data["date_time"], input_data["sensor_id"], input_data["value"])

            # ----------------------- GET SENSOR DATA -------------------
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

            # ----------------------- GET SENSOR LIST ------------------------
            elif input_data["action"] == "get-sensor-list":
                return user_data, service_get_sensor_list.get_sensor_list(self.mydb)

            # ------------------ GET LAST STATE SENSORS ----------------------
            elif input_data["action"] == "get-last-state-sensors":
                if "end_date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'end_date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, service_get_last_state_sensors.get_last_state_sensors(self.mydb, input_data["end_date"])

            # ----------------------- UPLOAD WAITING TIME --------------------
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

            # ---------------------------- NO SERVICE ------------------------
            else:
                json_error = '''{{
                    "error": "the action {} is not managed by the server"
                }}'''.format(input_data["action"])
                return user_data, json_error

