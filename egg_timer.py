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
    marker = seconds * 0.1
    
    print('Timer set for {0} minutes, or {1} seconds.'.format(minutes, seconds))
    
    for  i in range(1, seconds+1):
        print(i)
        time.sleep(1)
        # TODO Clear console
        # clear()
        # TODO SHOW MINUTES AND SECONDS IN FORMAT 00:00
        
    print(donemsg)
    
start_timer(5, 'Get your spoons ready! Almost done.', 'It\'s cooked!')
