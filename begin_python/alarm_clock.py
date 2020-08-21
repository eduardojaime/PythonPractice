# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6

@author: Eduardo Jaime
"""
# Displaying the Hour
import time

curr_time = time.localtime()

curr_hour = curr_time.tm_hour
curr_mins = curr_time.tm_min

time_of_day = 'afternoon'

if (curr_hour < 12):
    time_of_day = 'morning'
elif (curr_hour > 19):
    time_of_day = 'evening'
    
print('It\'s {0} with {1} mins in the {2}'.format(curr_hour, curr_mins, time_of_day))

if ((curr_hour > 6) or (curr_hour == 6 and curr_min > 0)):
    print('\a')
    print('It\'s time to get up!')
    time.sleep(2)