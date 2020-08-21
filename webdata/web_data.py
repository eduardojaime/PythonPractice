# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30

@author: Eduardo Jaime
"""
import urllib.request
import urllib.parse
# For error handling
from http import HTTPStatus
from urllib.error import HTTPError
from urllib.error import URLError
# Simple API to work with http verbs
import requests


# for requests module
def printResults(result):
    print("Result Code: {0}".format(result.status_code))
    print("Headers: {0}".format(result.headers))
    print("Content: {0}".format(result.content))
    print("Text: {0}".format(result.text))

# Simple request
url = "http://httpbin.org/xml"
result = urllib.request.urlopen(url)
# A request returns header and payload data
print("Result Code: {0}".format(result.status))
print("Headers: {0}".format(result.getheaders()))
# Returned as raw bytes
# print("Payload: {0}".format(result.read()))
# Returned as UTF8
print("Payload: {0}".format(result.read().decode('utf-8')))

# Sending Data to Web Services
# GET
url = "http://httpbin.org/get"

args = {
        "name" : "James",
        "is_author" : "true"
    }
# Encode parameters to be passed as part of url
data = urllib.parse.urlencode(args)
result = urllib.request.urlopen(url + "?" + data)

# Show results
print("Result Code: {0}".format(result.status))
print("Headers: {0}".format(result.getheaders()))
print("Payload: {0}".format(result.read().decode('utf-8')))

# POST
url = "http://httpbin.org/post"
data = data.encode()
result = urllib.request.urlopen(url, data=data)

# Show results
print("Result Code: {0}".format(result.status))
print("Headers: {0}".format(result.getheaders()))
print("Payload: {0}".format(result.read().decode('utf-8')))
print("\n")

# Handling Errors - 404 500

# url = "http://httpbin.org/html" # Works fine
# url = "http://httpbin.org/status/404" # HTTP ERROR
url = "http://no-such-server.org" # URL ERROR
try:
    result = urllib.request.urlopen(url)
    print("Result Code: {0}".format(result.status))
    if (result.getcode() == HTTPStatus.OK):
        print(result.read().decode('utf-8'))
except HTTPError as err:
    print("Error Code: {0}".format(err.code))
except URLError as err:
    print("Error Reason: {0}".format(err.reason))

# Using requests module
# HTTP GET request
url = "http://httpbin.org/xm"
result = requests.get(url)
printResults(result)

url = "http://httpbin.org/get"
data = {
       "key":"value"     
   }
result = requests.get(url, params=data)
printResults(result)

#HTTP POST request
url = "http://httpbin.org/post"
# data or header values
data = {
       "User-Agent":"value"     
}
# pass as data or headers
result = requests.post(url, data=data)
result = requests.post(url, headers=data)
# use this with a try catch to raise errors
# requests.raise_for_status()

printResults(result)





































