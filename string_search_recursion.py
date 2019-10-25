# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24

@author: Eduardo Jaime
"""

# Search a string in another string
# Count the number of times it appears

# Using brute force approach comparing one time for every character in the string
# if index is 0 then a match has been found
def string_search_brute_force(string, search_term):
    count = 0
    length = len(string)
    for i in range(0, length):
        index = string[i:length].find(search_term)
        if index == 0:
            count+=1
    # print(count)
    return count

# Using recursion and reducing the number of comparisons made
# if index >= 0 then a match is found and a substring is produced using the new index
# search is then repeated
def string_search_recursive(string, search_term, count):
    length = len(string)
    index = string[0:length].find(search_term)
    # count = 0
    if index >= 0:
        count = count + 1
        return string_search_recursive(string[index+1:length], search_term, count)
    else:
        # print(count)
        return count


string = "THIS IS AN EXAMPLE"
search_term = "IS"
# Expected 2
print(string_search_brute_force(string,search_term))
print(string_search_recursive(string, search_term, 0))
