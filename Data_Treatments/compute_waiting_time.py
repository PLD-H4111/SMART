import json
import http_methods
import sensor_preprocessing
import datetime
import numpy
import time

def send_waiting_time(waiting_time,timsetamp,restaurant):
    params = {
        "action": "upload-waiting-time",
        "waiting_time": waiting_time,
        "timestamp": timsetamp,
        "restaurant": restaurant
        }
    http_methods.send_data(params)


person_counts = { #per restaurant per position
    "8": {
        "1": 10,
        "2": 25,
        "3": 25,
        "4": 40
    }
}

speed = 8 #persons per min

interval = 10 #sec

if __name__ == "__main__":
    persons = {}

    while True:

        try:
            sensors_state_per_restaurant = sensor_preprocessing.get_sensors_state_per_restaurant()
        except Exception as ex:
            print(ex)
            continue

        for restaurant_id, restaurant in sensors_state_per_restaurant.items():
            if restaurant_id == "8":
                persons[restaurant_id] = 0
                for sensor_type, sensors in restaurant.items():
                    for position, state in sensors.items():
                        if sensor_type == "Infrarouge" and state != 1:
                            next_pos = [str(int(position)+1), str(int(position)+2)]
                            if all(n in sensors and sensors[n] == 1 for n in next_pos):
                                state = 1
                            else:
                                between_pos = next_pos = [str(int(position)-1), str(int(position)+1)]
                                if all(n in sensors and sensors[n] == 1 for n in between_pos):
                                    state = 1
                        elif sensor_type == "Ultrason" and state < 0.1:
                            state = 0


                        if state >= 0:
                            persons[restaurant_id] += person_counts[restaurant_id][position]*state
                        elif state == -1: #Too noisy
                            persons[restaurant_id] += person_counts[restaurant_id][position]*0.5
            else:
                if restaurant_id not in persons:
                    persons[restaurant_id] = 0

                persons[restaurant_id] -= (speed/60)*interval
                if persons[restaurant_id] < 0:
                    persons[restaurant_id] = 0

                persons[restaurant_id] += numpy.random.poisson((speed/60)*interval)


        timestamp = datetime.datetime.now()
        waiting_time = {}
        for restaurant_id in persons:
            waiting_time[restaurant_id] = persons[restaurant_id] / speed
            send_waiting_time(waiting_time[restaurant_id], timestamp, restaurant_id)

        print(waiting_time)
        time.sleep(interval)
