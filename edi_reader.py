# -*- coding: utf-8 -*-
"""
Created on Mon Dec  2

Reading and Formating EDI file

#edi_line = "BAK^06^AD^0000814767^20180928^^^^0476550159^20180928".split('^')

@author: Eduardo Jaime
"""
import tkinter
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()

columns = ["Type", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]  

for i in range(0, len(columns)):
    print(columns[i].ljust(14), end="")
print('\n')

root.wm_withdraw()
name = askopenfilename(initialdir="C:/", filetypes=(("EDI Txt","*.txt"), 
                                                    ("All files","*.*")), 
    title="Select an EDI File")
    
with open(name, 'r') as file:
    line = file.readline()
    while line:
        line = file.readline()
        edi_line = line.split('^')
        if len(edi_line) == 1:
            edi_line = line.split('*')
        for i in range(0, len(edi_line)):
            print(edi_line[i].ljust(14), end="")
        print('\n')

root.destroy()