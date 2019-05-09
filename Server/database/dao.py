#!/usr/bin/python3
# -*- coding: utf-8 -*-


import mysql.connector



"""database_connector = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="toorTOOR2019!",
    database="main"
)"""

"""
database_connector = mysql.connector.connect(
    host="sql7.freemysqlhosting.net",
    user="sql7291089",
    passwd="bbf4tfEUn1",
    database="sql7291089",
    use_pure=True
)
"""


def select_all_restaurants(database_connector):
    query = "select * from Restaurant;"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result
    
def select_restaurant(database_connector, restaurant_id):
    query = "select * from Restaurant where PK_idRestaurant=" + str(restaurant_id) + ";"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def select_last_waiting_time(database_connector, restaurant_id):
    query = "select * from WaitingTime where FK_restaurant=" + str(restaurant_id) + " ORDER BY date DESC LIMIT 1;"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result

def select_actual_restaurant_availability(database_connector, restaurant_id):
    query = "select * from RestaurantAvailabilities where FK_restaurant=" + str(restaurant_id) + " and openingTime <= Time(now()) and closingTime >= Time(now()) and Date(now()) = date(date)"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result


def select_restaurant_availabilities(database_connector, restaurant_id, date):
    query = "select * from RestaurantAvailabilities where FK_restaurant=" + str(restaurant_id) + " and Date(date) = '" + date + "';"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def select_waiting_times(database_connector, restaurant_id, date):
    query = "select * from WaitingTime where FK_restaurant=" + str(restaurant_id) + " and Date(date) = '" + date + "';"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result


def select_admin(database_connector, login, passwd):
    query = "select * from Admin where login='" + login + "' and password = '" + passwd + "';"
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchone()
    return result
    
def insert_restaurant_event(database_connector, title, start, end, restaurant_id, content):
    insert_query = """ INSERT INTO `Event` (`name`, `beginningDate`, `endingDate`, `FK_restaurant`, `eventDescription`)
                               VALUES (%s,%s,%s,%s,%s)"""
    insert_tuple = (title, start, end, restaurant_id, content)
    cursor = database_connector.cursor(prepared=True)
    cursor.execute(insert_query, insert_tuple)
    database_connector.commit()



def select_restaurant_events(database_connector, restaurant_id, date):
    """ """
    query = "select name, eventDescription, beginningDate, endingDate from Event where FK_Restaurant = " + restaurant_id
    print(query)
    cursor = database_connector.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    return result;
    
    

def select_restaurants_events(database_connector):
    """ """
    query = "select PK_idEvent, Event.name, beginningDate, endingDate, Restaurant.name from Event, Restaurant where Restaurant.PK_idRestaurant = Event.FK_Restaurant"
    cursor = database_connector.cursor()    
    cursor.execute(query)
    result = cursor.fetchall()
    return result;


def select_event_details(database_connector, event_id):
    """ """       
    query = "select Event.name, eventDescription, beginningDate, endingDate, Restaurant.name from Event, Restaurant where Restaurant.PK_idRestaurant = Event.FK_Restaurant and PK_idEvent = " + event_id
    cursor = database_connector.cursor()    
    cursor.execute(query)
    result = cursor.fetchall()
    return result;

