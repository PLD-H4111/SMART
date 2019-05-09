#!/usr/bin/python3
# -*- coding: utf-8 -*-


import json
import dao



def login_admin(user_data, username, passwd):
    """ """
    admin = dao.select_admin(username, passwd)
    json_result = ""
    if admin != None:
        user_data = {
            "id": admin[0]
        }
        json_result = """{
            "authentication": "success",
            "success": 1
        }"""
    else:
        json_result = """{
            "authentication": "failure",
            "success": 0
        }"""
    return user_data, json_result
