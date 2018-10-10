# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:41:23 2018

@author: Maysa
"""

#Retrieve 3 integers for the variables x, y, and z from the user
x = int(input("Please enter an integer for variable x: "))
y = int(input("Please enter an integer for variable y: "))
z = int(input("Please enter an integer for variable z: "))

#if x is odd, then evaluate whether x is the largest number and print that

if x%2 != 0 and x > y and x > z:
    print("\nx is the largest odd number!")
elif y%2 != 0 and y > x and y > z:
    print("\ny is the largest odd number!")
elif z%2 != 0 and z > x and z > y: 
    print("\nz is the largest odd number!")
elif x%2 == 0 and y%2 == 0 and z%2 ==0:
    print("\nSorry, none of these numbers are odd!")
else:
    print("\nHmm...none of these is the largest because they're all equal!")
    