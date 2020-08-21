# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31

@author: Eduardo Jaime
"""
# Parsing JSON data
import json
from json import JSONDecodeError
import requests

jsonStr = '''{
                "name":"Reuben",
                "ingredients": [
                        "Sauerkraut",
                        "Pickles"
                ],
                "toasted":"true",
                "price":8.99
            }'''

data = json.loads(jsonStr)
print("Sandwich: " + data['name'])
if (data['toasted']):
    print("Toasted!")
for ingredient in data['ingredients']:
    print(ingredient)

print('\n')

# Serializing object into JSON
pythonData = {
                "name":"Reuben",
                "ingredients": [
                        "Sauerkraut",
                        "Pickles"
                ],
                "toasted":True,
                "price":8.99
            }

print("JSON Data")
jsonStr = json.dumps(pythonData, indent=4)
print(jsonStr)

print('\n')

# Handling Errors
jsonStr = '''{
                "name":"Reuben",
                "ingredients": [
                        "Sauerkraut",
                        "Pickles"
                // MISSING ],
                "toasted":"true",
                "price":8.99
            }'''

# Strongly recommended best practice
try:
    data = json.loads(jsonStr)
except JSONDecodeError as err:
    print("Error while decoding:")
    print(err.msg)
    print(err.lineno, err.colno)


print('\n')

# Using JSON in requests
    
url = "http://httpbin.org/json"
result = requests.get(url)
# built in decoder
dataobj = result.json()
print(json.dumps(dataobj, indent=4))
# access by key
print("There are {0} slides in the slideshow.".format(len(dataobj['slideshow']['slides'])))