# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31

@author: Eduardo Jaime
"""
# SAX Parsing Model
import xml.sax
import requests
import xml.dom.minidom

# ContentHandler class needed to define what to do with each element
class MyContentHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.slideCount = 0
        self.itemCount = 0
        
    def startElement(self, tagName, attrs):
        if tagName == "slideshow":
            print("Title: {0}".format(attrs['title']))
    
    def startDocument(self):
        print("About to start")
        
    def endDocument(self):
        print("Finishing up!")

url = "http://httpbin.org/xml"
result = requests.get(url)
#print(result.text)

handler = MyContentHandler()
xml.sax.parseString(result.text, handler)
print("There were {0} slide elements.".format(handler.slideCount))

print('\n')

# DOM API - similar to .NET System.XML
url = "http://httpbin.org/xml"
result = requests.get(url)
#print(result.text)
# Parse content into DOM structure to inspect it
domtree = xml.dom.minidom.parseString(result.text)
rootnode = domtree.documentElement

print(rootnode.nodeName)
print("Title: {0}".format(rootnode.getAttribute('title')))

items = domtree.getElementsByTagName("item")
print("There are {0} items in the document".format(items.length))

# Unlike SAX, with DOM we can also modify the XML document
newItem = domtree.createElement("item")
newItem.appendChild(domtree.createTextNode("Some Text"))
firstSlide = domtree.getElementsByTagName("slide")[0]
firstSlide.appendChild(newItem)
print("New element added")
# new item count
items = domtree.getElementsByTagName("item")
print("There are {0} items in the document".format(items.length))
print()