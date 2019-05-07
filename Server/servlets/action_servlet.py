#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import mysql.connector

import service1
import service2



class ActionServlet:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="toorTOOR2019!",
            database="main"
        )
    
    def fetch(self, input_data):
        """ """
        print("action servlet:", input_data["action"][0])
        print(input_data)
        
        if "action" not in input_data:
            json_error = '''{
                "error": "there's no 'action' parameter in the parameters passed as input"
            }'''
            return json_error
        else:
            if input_data["action"][0] == "get-restaurants-list":    
                return service1.get_restaurants(self.mydb)
            elif input_data["action"][0] == "get-restaurant-details":
                if "restaurants[]" not in input_data:
                    json_error = '''{
                        "error": "there's no 'restaurants[]' parameter in the parameters passed as input"
                    }'''
                    return json_error
                if "date" not in input_data:
                    json_error = '''{
                        "error": "there's no 'date' parameter in the parameters passed as input"
                    }'''
                    return json_error
                else:
                    return service2.get_restaurants_details(self.mydb, input_data["restaurants[]"][0], input_data["date"][0])
            else:
                pass

