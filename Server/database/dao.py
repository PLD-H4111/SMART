#!/usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector
    
database_connector = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7290893",
    passwd="bwykkiQ1WX",
    database="sql7290893",
    use_pure=True
)

def select_all_restaurants():
    request = "select * from Restaurant;"
    cursor = database_connector.cursor()
    cursor.execute(request)
    result = cursor.fetchall()
    return result
    
def select_restaurant(restaurant_id):
    request = "select * from Restaurant where PK_idRestaurant=" + str(restaurant_id) + ";"
    cursor = database_connector.cursor()
    cursor.execute(request)
    result = cursor.fetchone()
    return result


def select_last_waiting_time(restaurant_id):
    request = "select * from WaitingTime where FK_restaurant=" + str(restaurant_id) + " ORDER BY date DESC LIMIT 1;"
    cursor = database_connector.cursor()
    cursor.execute(request)
    result = cursor.fetchone()
    return result

def select_actual_restaurant_availability(restaurant_id):
    request = "select * from RestaurantAvailabilities where FK_restaurant=" + str(restaurant_id) + " and openingTime <= Time(now()) and closingTime >= Time(now()) and Date(now()) = date(date)"
    cursor = database_connector.cursor()
    cursor.execute(request)
    result = cursor.fetchone()
    return result
    
    
    
#print( select_actual_restaurant_availability(11) )
#print( select_last_waiting_time(1) )

  
