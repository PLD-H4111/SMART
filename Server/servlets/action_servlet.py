#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import mysql.connector

import service1
import service2
import service3
import service4
import service5
import sensor_upload
import service_get_data_sensors
import service_get_sensor_list


# TODO: verifier l'authentification pour les services sensibles
# i.e user_data == None


class ActionServlet:
    def __init__(self):
        """self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toorTOOR2019!",
            database="main"
        )"""
        self.mydb = mysql.connector.connect(
            host="sql7.freemysqlhosting.net",
            user="sql7290893",
            passwd="bwykkiQ1WX",
            database="sql7290893",
            use_pure=True
        )
    
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
                return user_data, service1.get_restaurants(self.mydb)
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
                    return user_data, service2.get_restaurants_details(self.mydb, input_data["restaurants"], input_data["date"])
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
                    return service3.login(self.mydb, user_data, input_data["login"], input_data["password"])
            elif input_data["action"] == "create-restaurants-events":
                print(input_data)
                return user_data, service4.create_restaurants_event(self.mydb,
                                                                   input_data["title"],
                                                                   input_data["content"],
                                                                   input_data["start"],
                                                                   input_data["end"],
                                                                   input_data["restaurants"])
            elif input_data["action"] == "get-restaurant-events":
                return user_data, service5.get_restaurant_event(self.mydb, input_data["restaurant"], input_data["date"])
            elif input_data["action"] == "get-all-restaurants-events":
                return user_data, service5.get_all_restaurants_events(self.mydb)
            elif input_data["action"] == "get-event-details":
                return user_data, service5.get_event_details(self.mydb, input_data["event"])
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
            else:
                json_error = '''{{
                    "error": "the action {} is not managed by the server"
                }}'''.format(input_data["action"])
                return user_data, json_error

