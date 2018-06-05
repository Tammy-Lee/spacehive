# -*- coding: utf-8 -*-
"""
create on 2018-06-05 23:46
author @66492
"""
import pymongo

from spacehive.settings import config

_mongo_client = pymongo.MongoClient(config.MONGO_URI)
mongodb = _mongo_client[config.MONGO_DBNAME]
_mongo_auth = config.MONGO_AUTH
if _mongo_auth:
    mongodb.authenticate(**_mongo_auth)
