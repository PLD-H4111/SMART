#!/bin/python3


from collections import OrderedDict
import requests
import json





def get_data():
	data_source_url = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset"
	PARAMS = {'userKey': "0"}
	r = requests.get(url = data_source_url, params = PARAMS)
	data = r.json()
	return data



def send_data(result):
	destination_url = "https://candidate.hubteam.com/candidateTest/v3/problem/result"#?userKey=de754f3d42b28450079f35868267"
	destination_url = "http://127.0.0.1"
	PARAMS = {'userKey': "0"}
	result = json.dumps(result, sort_keys=False, indent=4)
	r = requests.post(url = destination_url, headers={"content-type": "application/json;charset=utf-8"}, data = result, params=PARAMS) 
	pastebin_url = r.text 
	print("The pastebin URL is:%s"%pastebin_url) 



send_data("1, 2, 3, viva l'Algérie !")
