#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def create_restaurants_event(database, title, content, start, end, restaurants):
    """ """
    mycursor = database.cursor(prepared=True)
    insert_query = """ INSERT INTO `Event` (`name`, `beginningDate`, `endingDate`, `FK_restaurant`, `eventDescription`)
                               VALUES (%s,%s,%s,%s,%s)"""
                               
    for rid in restaurants:
        insert_tuple = (title, start, end, rid, content)
        mycursor.execute(insert_query, insert_tuple)
        database.commit()
    return '''{"success": 1}''';

