#!/usr/bin/env python3

import gpiozero, gpiozero.pins.pigpio
from signal import pause
import time
import datetime
import requests, json

server_ip = "192.168.0.103"
server_port = 8080
server_url = "http://%s:%s/action_servlet" % (server_ip, server_port)

gpiozero.Device.pin_factory = gpiozero.pins.pigpio.PiGPIOFactory()

IR_sensors = {
        19: {"id": 3},
        20: {"id": 2},
        21: {"id": 1}
        }

IR_devices = []

IR_leds = {
        19: gpiozero.LED(22),
        20: gpiozero.LED(23),
        21: gpiozero.LED(24)
        }

US_sensors = {
        14: {"id": 4, "echo": 14, "trigger": 15}
        }

US_devices = []

pending_data = []

def send_data():
    try:
        while len(pending_data) != 0:
            json_data = json.dumps({"action":"sensor-upload", **pending_data[0]}, sort_keys=False)

            response = requests.post(url=server_url, headers={"Content-type": "application/json"}, data=json_data, timeout=5)

            if response.status_code == 200:
                json_response = json.loads(response.text)
                if json_response["status"] == "ok":
                    pending_data.pop(0)
                else:
                    print("Error while sending data. Status code :", response.status_code, "/ JSON Response :", json_response)
                    return
            else:
                print("Error while sending data. Status code :", response.status_code, "/ Response :", response.text)
                return
    except Exception as ex:
        print("Error while sending data :", ex)
        return

def process_IR(device):
    gpio = device.pin.number
    sensor_id = IR_sensors[gpio]["id"]
    date_time = str(datetime.datetime.now())

    data = {
        "date_time": date_time,
        "sensor_id": sensor_id,
        "value": int(device.value)
        }

    print("IR event :", data)
    if data["value"]:
        IR_leds[gpio].on()
    else:
        IR_leds[gpio].off()

    pending_data.append(data)

def process_US(device):
    gpio = device.pin.number
    sensor_id = US_sensors[gpio]["id"]
    date_time = str(datetime.datetime.now())

    data = {
        "date_time": date_time,
        "sensor_id": sensor_id,
        "value": int(device.distance*1000)
        }

    print("US event :", data)
    pending_data.append(data)

if __name__ == "__main__":
    for gpio in IR_sensors:
        device = gpiozero.Button(gpio, active_state=True, pull_up=None, bounce_time=0.01)
        device.when_pressed = process_IR
        device.when_released = process_IR
        if not int(device.value):
            IR_leds[gpio].off()

        IR_devices.append(device)

    for gpio, sensor in US_sensors.items():
        device = gpiozero.DistanceSensor(sensor["echo"], sensor["trigger"], max_distance=5)
        US_devices.append(device)

    while True:
        for device in US_devices:
            process_US(device)
        send_data()
        time.sleep(1)

    pause()

