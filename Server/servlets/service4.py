#!/usr/bin/python3
# -*- coding: utf-8 -*-

import json

def create_restaurants_event(database,title, content, start, end, restaurants):
    """ """
    request = "insert into main`.`Event` (`PK_idEvent`, `name`, `beginningDate`, `endingDate`, `FK_restaurant`, `eventDescription`) "
                                          + " VALUES (DEFAULT, '"+title+"' , '"+start+"' , '"+end+ "' , '" +restaurants+ "' , '" +content+"'); 
    mycursor = database.cursor()    
    mycursor.execute(request)
    
    return '''{"success": 1}''';

