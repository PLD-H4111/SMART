#!/bin/python3

import requests
import json

server_ip = "192.168.0.103"
server_port = 8080
server_url = "http://%s:%s/action_servlet" % (server_ip, server_port)

def send_data(result):
    try:
        json_data = json.dumps(result, sort_keys=False, default=str)

        response = requests.post(url=server_url, headers={"Content-type": "application/json"}, data=json_data, timeout=5)

        if response.status_code != 200:
            print("Error while sending data. Status code :", response.status_code, "/ Response :", response.text)

        return response.text
    except Exception as ex:
        print("Error while sending data :", ex)
        return None
