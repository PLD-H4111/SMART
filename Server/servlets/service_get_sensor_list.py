#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def get_sensor_list(database):

    request = """
    select FK_restaurant, type, position
    from Sensor, SensorType
    where FK_sensorType = PK_idSensorType
    """

    cursor = database.cursor()
    cursor.execute(request)
    result = cursor.fetchall()

    data = {"sensors_per_restaurant": {}}

    for sensor in result:
        restaurant_id = int(sensor[0])
        sensor_type = str(sensor[1])
        position = int(sensor[2])

        if restaurant_id not in data["sensors_per_restaurant"]:
            data["sensors_per_restaurant"][restaurant_id] = {}

        if sensor_type not in data["sensors_per_restaurant"][restaurant_id]:
            data["sensors_per_restaurant"][restaurant_id][sensor_type] = []

        data["sensors_per_restaurant"][restaurant_id][sensor_type].append(position)

    return json.dumps(data)

#{
    #"sensors_per_restaurant": {
        #1: {
            #"Infrarouge": [0, 3, 5]
            #},
        #8: {
            #"Infrarouge": [1, 6, 8],
            #"Ultrason": [2, 3]
            #}
        #}
#}
