# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2

Solution to namedtuples problem:
    
Given:  
    n students
    column names in any order
    a list of n students
    
Calculate the avg of the marks in the list
    
@author: Eduardo Jaime
"""

from collections import namedtuple

# Total number of students
n = int("1")

# Columns can be input in any order
columns = "ID MARKS NAME CLASS"

sumMarks = 0

Student = namedtuple("Student", columns.split())

for i in range(0, n):
    # Each input will represent a student
    values = "1 97 Raymond 7".split()
    std = Student(values[0], values[1], values[2], values[3])
    sumMarks +=  int(std.MARKS);

# Show the avg with two decimal digits
avg = sumMarks / n
print(format(avg, '.2f'))