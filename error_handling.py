# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9

@author: Eduardo Jaime
"""
# Basic try-except structure
try:
    input_text = input('Code will break if you enter a letter or a symbol:')
    input_int - int(input_text)
except:
    print('Some error happened!')
print('\n')

# Exceptions can have more than one handler
try_again = True
while try_again == True:
    try:
        input_text = input('Enter a number from 1 to 5:')
        input_int = int(input_text)
        if input_int > 5 or input_int < 1:
            print('Invalid input, please enter a number from 1 to 5')
        else:
            print('You entered: ', input_text)
            try_again = False
    except ValueError:
        print('Invalid number!')
        
print('Program ended')
print('\n')

