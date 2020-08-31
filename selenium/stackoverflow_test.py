# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25

@author: Eduardo Jaime
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

url = "https://stackoverflow.com/questions"

driver = webdriver.Chrome()

driver.get(url)
driver.maximize_window()

print("Visiting " + driver.title)

page_source = driver.page_source

elem = driver.find_element_by_class_name("question-hyperlink")
print(elem.text)
print("\n")

searchbox = driver.find_element_by_name("q")

print("Let's ask what selenium is...")
print("\n")

searchbox.clear()
searchbox.send_keys("What is selenium?")
searchbox.send_keys(Keys.ENTER)

excerpt = driver.find_element_by_class_name("excerpt")
print(excerpt.text)
print("\n")

print("Great, we are done here! Good Night")

driver.close()