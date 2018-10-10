# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 20:16:23 2018

@author: Maysa
"""

###################
# EXAMPLE: while loops 
# Try expanding this code to show a sad face if you go right
# twice and flip the table any more times than that. 
# Hint: use a counter
###################
#n = input("You are in the Lost Forest\n****************\n****************\n :)\n****************\n****************\nGo left or right? ")
#while n == "right" or n == "Right":
#    n = input("You are in the Lost Forest\n****************\n******       ***\n  (╯°□°）╯︵ ┻━┻\n****************\n****************\nGo left or right? ")
#print("\nYou got out of the Lost Forest!\n\o/")

counter = 0
n = input("You are in the Lost Forest.\n*******************\n*******************\n :)\n*******************\n*******************\nGo left or right? ")
while n == "right" or n == "Right" or n == "RIGHT": 
    counter = counter + 1
    if counter <= 2:
        n = input("You are in the Lost Forest.\n*******************\n*******************\n :)\n*******************\n*******************\nGo left or right? ")
    else:
        n = input("You are STILL in the Lost Forest.\n*******************\n*******************\n :(\n*******************\n*******************\nDo you maybe want to learn from your mistakes and try something new? ")
print("\nYou got out! Good job, doggy. WOOF")