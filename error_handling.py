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
    except KeyboardInterrupt:
        exit_option = input('Are you sure you want to Exit? Y or N')
        if exit_option.upper() == 'Y':
            try_again = False
            print('Ending program...')
print('\n')

try_again = True
while try_again == True:
    try:
        input_text = input('Enter a number from 1 to infinity, to see its Times Table:')
        input_int = int(input_text)
        if input_int <= 0:
            print('Negative numbers are not allowed')
        else:
            times_val = 1
            while times_val <= 10:
                print(input_int, 'times', times_val, 'equals', input_int * times_val)
                times_val = times_val + 1
            exit_option = input('Press any key to try again, or press E to exit.')
            if exit_option.upper() == 'E':
                try_again = False
            
    except ValueError:
        print('Invalid number! Enter a numeric value')
        
print('Program ended')
print('\n')

