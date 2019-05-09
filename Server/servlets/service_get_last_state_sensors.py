#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def get_last_state_sensors(database,end_date):
    request = """
    SELECT FK_restaurant, position, dateTime, measure
    FROM (SELECT * FROM Measure m2 where dateTime <= "{}" ORDER BY dateTime DESC, PK_idMeasure DESC) m1
    JOIN Sensor ON m1.FK_Sensor = Sensor.PK_idSensor
    GROUP BY FK_sensor
    """.format(end_date)

    cursor = database.cursor()
    cursor.execute(request)
    result = cursor.fetchall()

    data = {"last_state_sensors": {}}

    for measure in result:
        restaurant_id = int(measure[0])
        position = int(measure[1])
        datetime = str(measure[2])
        value = int(measure[3])

        if restaurant_id not in data["last_state_sensors"]:
            data["last_state_sensors"][restaurant_id] = {}

        data["last_state_sensors"][restaurant_id][position] = {
            "datetime": datetime,
            "value": value
            }

    return json.dumps(data)

