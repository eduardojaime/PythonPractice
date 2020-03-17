# -*- coding: utf-8 -*-
"""
Created on Wed Dec 18

Objective: Given a log file, get all lines containing a specific ID

@author: egan
"""
import tkinter
from tkinter.filedialog import askopenfilename

root = tkinter.Tk()
root.wm_withdraw()

name = askopenfilename(initialdir="C:/", filetypes=(("Log Files", "*.log"),
                                                    ("All Files","*.*")),
                        title="Select a Log file")

with open(name, 'r') as file:
    line = file.readline()
    print(line)
    while line:
            file.readline()


