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

def get_data_from_sensors(database,start_date,end_date):
    
    time_format = "%Y-%m-%d %H:%M:%S"
    
    request = """
    select measure,datetime,position,type
    from Measure,Sensor,SensorType
    where "{}" < datetime and "{}" > datetime and
    FK_sensor = PK_idSensor and FK_sensorType = PK_idSensorType;
    """.format(start_date,end_date)

    mycursor = database.cursor()
    mycursor.execute(request)
    myresult = mycursor.fetchall()

    data = {"data": []}
    for donnee in myresult:
        data["data"].append({"measure": str(donnee[0]), "datetime": "{}".format(donnee[1]), "position": str(donnee[2]), "type": donnee[3]})

    data = json.dumps(data)
    
    return data
