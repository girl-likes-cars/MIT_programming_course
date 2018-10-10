# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:41:23 2018

@author: Maysa
"""

#find the root and power of any integer
#power must be between 0 and 6 (aka, 1-5)

#start by seeing if the integer has a power of 2
integer = int(input("Give me an integer: "))
power = int(5)

#as long as integer root is NOT a whole number, try a smaller power
while (integer**(1/power)).is_integer() == False:
    power = power - 1
    #once you reach a power smaller than 2, print "Sorry, no solution" and break 
    if power == 1:
        print("Sorry, there is no solution")
        break
#once the root of the integer is a whole number, print the result and prompt user to go again
if integer**(1/power).is_integer() == True:
    print("Your root is",int(integer**(1/power)),"and your power is",power)
else:
    prompt = input("Go again? (Y/N)")

while prompt == "Y":
    integer = int(input("Give me an integer: "))
    power = int(5)
    while (integer**(1/power)).is_integer() == False:
        power = power - 1
        #once you reach a power smaller than 2, print "Sorry, no solution" and break 
        if power == 1:
            print("Sorry, there is no solution")
            break
    #once the root of the integer is a whole number, print the result and prompt user to go again
    if integer**(1/power).is_integer() == True:
        print("Your root is",int(integer**(1/power)),"and your power is",power)
    else:
        prompt = input("Go again? (Y/N)")