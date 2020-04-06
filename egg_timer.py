# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 

@author: Eduardo Jaime
"""
from os import system, name
import time

# https://www.geeksforgeeks.org/clear-screen-python/
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear') 

# Egg timer program
def start_timer(minutes, almostmsg, donemsg):
    # Show almost done message at 90% done
    seconds = minutes * 60
    marker = seconds * 0.9 # 90% done
    
    print('Timer set for {0} minutes, or {1} seconds.'.format(minutes, seconds))
    
    for i in range(1, seconds):
        time.sleep(1)
        if i >= marker:
          print(i, almostmsg)
        else:
            print(i)
        # TODO Clear console
        # clear()
        # TODO SHOW MINUTES AND SECONDS IN FORMAT 00:00
    
    time.sleep(1) # sleep for an extra second then show completion
    print(donemsg)
    
# User configurable timer
time_text = input('Enter time in minutes')
time_int = int(time_text)
start_timer(time_int, 'Get your spoons ready! Almost done.', 'It\'s cooked!')

