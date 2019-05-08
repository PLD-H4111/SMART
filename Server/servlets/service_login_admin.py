#!/usr/bin/python3
# -*- coding: utf-8 -*-


from importlib import reload
import sys
sys.path.insert(0, './database/')
reload(sys)

import json
import dao



def login_admin(user_data, username, passwd):
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
