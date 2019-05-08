#!/usr/bin/python3
# -*- coding: utf-8 -*-

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

def get_sensor_list(database):
    
    request = """
    select position,type
    from Sensor,SensorType
    where FK_sensorType = PK_idSensorType;
    """
    
    mycursor = database.cursor()
    mycursor.execute(request)
    myresult = mycursor.fetchall()
    
    capteurs = {"capteurs": []}
    for capteur in myresult:
        capteurs["capteurs"].append({"position": str(capteur[0]), "type": capteur[1]})

    capteurs = json.dumps(capteurs)
    
    return capteurs
