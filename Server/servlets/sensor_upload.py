#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def sensor_upload(database, timestamp, sensor_id, value):
    """ """
    try:
        insert_query = "INSERT INTO Measure (dateTime, FK_sensor, measure) VALUES (%s, %s, %s)"
        cursor = database.cursor()
        cursor.execute(insert_query, (timestamp, sensor_id, value))
        database.commit()
        return '{"status": "ok"}'
    except Exception as ex:
        return "An error occurred : %s" % ex
