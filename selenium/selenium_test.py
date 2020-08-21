# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11

Tutorial:       https://selenium-python.readthedocs.io/getting-started.html#simple-usage
ChromeDriver:   https://sites.google.com/a/chromium.org/chromedriver/downloads

@author: Eduardo Jaime
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Using Chrome
# driver = webdriver.Chrome()

# Using Firefox
driver = webdriver.Firefox()

driver.get("http://www.python.org")

page_title = driver.title
page_source = driver.page_source

assert "Python" in page_title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "No results found." not in page_source

# Close Session
driver.close()