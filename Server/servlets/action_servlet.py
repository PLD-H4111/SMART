#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import mysql.connector

import service1
import service2
import service3
import service4
import service5



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
            database="sql7290893 "
        )
    
    def fetch(self, user_data, input_data):
        """ """
        print("action servlet:", input_data["action"][0])
        print(input_data)
        
        if "action" not in input_data:
            json_error = '''{
                "error": "there's no 'action' parameter in the parameters passed as input"
            }'''
            return user_data, json_error
        else:
            if input_data["action"][0] == "get-restaurants-list":    
                return user_data, service1.get_restaurants(self.mydb)
            elif input_data["action"][0] == "get-restaurant-details":
                if "restaurants[]" not in input_data:
                    json_error = '''{
                        "error": "there's no 'restaurants[]' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                elif "date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'date' parameter in the parameters passed as input"
                    }'''
                    return user_data, json_error
                else:
                    return user_data, service2.get_restaurants_details(self.mydb, input_data["restaurants[]"][0], input_data["date"][0])
            elif input_data["action"][0] == "admin-login":
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
                    return service3.login(self.mydb, user_data, input_data["login"][0], input_data["password"][0])
            elif input_data["action"][0] == "create-restaurants-news":
                return user_data, service4.create_restaurants_event(input_data["title"][0], 
                                                                   input_data["content"][0],
                                                                   input_data["start"][0],
                                                                   input_data["end"][0],
                                                                   input_data["restaurants[]"][0])
            elif input_data["action"][0] == "get-restaurant-news":
                return user_data, service5.get_restaurant_event(input_data["restaurant"][0], input_data["date"][0])
            elif input_data["action"][0] == "get-all-restaurants-news":
                return user_data, service5.get_all_restaurants_event()
            elif input_data["action"][0] == "get-event-details":
                return user_data, service5.get_event_details(input_data["event"][0])
            else:
                json_error = '''{{
                    "error": "the action {} is not managed by the server"
                }}'''.format(input_data["action"][0])
                return user_data, json_error

