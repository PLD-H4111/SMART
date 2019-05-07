#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json



def login(database, user_data, username, passwd):
    """ """
    json_result = ""
    if username == "1" and passwd == "2":
        user_data = {
            "id": 42
        }
        json_result = """{
            "authentification": "success",
            "success": 1
        }"""
    else:
        json_result = """{
            "authentification": "failure",
            "success": 0
        }"""
    return user_data, json_result
