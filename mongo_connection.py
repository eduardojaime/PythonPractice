# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2

Using Pymongo to connect to a Mongo DB 

@author: Eduardo Jaime
"""

from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient("MONGODB")
db=client.admin