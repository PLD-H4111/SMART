#!/usr/bin/python3
# -*- coding: utf-8 -*-

from importlib import reload
import sys
sys.path.insert(0, './database/')
reload(sys)

import json
import dao




def create_restaurants_event(database, title, content, start, end, restaurants_ids):
    """ """
    for restaurant_id in restaurants_ids:
        dao.insert_restaurant_event(title, start, end, restaurant_id, content)
    return '''{"success": 1}''';


