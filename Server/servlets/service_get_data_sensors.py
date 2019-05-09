#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def get_data_from_sensors(database,start_date,end_date):
    request = """
    select FK_restaurant, position, datetime, measure
    from Measure, Sensor
    where datetime >= "{}" and datetime < "{}" and
    FK_sensor = PK_idSensor;
    """.format(start_date,end_date)

    cursor = database.cursor()
    cursor.execute(request)
    result = cursor.fetchall()

    data = {"data_per_restaurant": {}}

    for measure in result:
        restaurant_id = int(measure[0])
        position = int(measure[1])
        datetime = str(measure[2])
        value = int(measure[3])

        if restaurant_id not in data["data_per_restaurant"]:
            data["data_per_restaurant"][restaurant_id] = {}

        if position not in data["data_per_restaurant"][restaurant_id]:
            data["data_per_restaurant"][restaurant_id][position] = []

        data["data_per_restaurant"][restaurant_id][position].append({
            "datetime": datetime,
            "value": value
            })

    return json.dumps(data)

