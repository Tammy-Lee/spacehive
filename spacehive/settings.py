# -*- coding: utf-8 -*-
"""
create on 2018-06-05 23:40
author @66492
"""
class Config(object):
    MONGO_URI = "mongodb://localhost:27017"
    MONGO_DBNAME = "spacehive"
    MONGO_AUTH = {}

    COL_TEST = "test"


config = Config
