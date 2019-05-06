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
        if "action" not in input_data:
            # pas la bonne structure de l'input data
            pass

        print("action servlet:", input_data["action"][0])
        
        if input_data["action"][0] == "get-restaurants-list":    
            return service1.get_restaurants(self.mydb)
        elif input_data["action"][0] == "get-restaurant-details":
            return service2.get_restaurant_details(self.mydb, input_data["id"][0], input_data["date"][0])
        else:
            pass

