#!/usr/bin/python3
# -*- coding: utf-8 -*-

import datetime
from datetime import date

"""
from importlib import reload
import sys
sys.path.insert(0, '../database/')
reload(sys)
#import bdr
=======
import bdr
"""

import json

def upload_waiting_time(database,waiting_time,timestamp,restaurant):
    try:
        insert_query = "INSERT INTO WaitingTime (date, FK_restaurant, waitingTime) VALUES (%s, %s, %s)"
        cursor = database.cursor()
        cursor.execute(insert_query, (timestamp, restaurant, waiting_time))
        database.commit()
        return '{"status": "ok"}'
    except Exception as ex:
        return "An error occurred : %s" % ex
