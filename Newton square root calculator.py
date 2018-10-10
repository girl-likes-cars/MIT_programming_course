# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 16:52:15 2018

@author: Maysa
"""

#Set the epsilon and the square root you want to find
#Pick a random starting point for your guess (let's say, guess/2)

epsilon = 0.01
k = int(input("Give me a number whose square root you want to find! "))
guess = k/2.0
iterations = 0
while guess*guess - k >= epsilon:
    guess = guess - ((guess**2 - k)/(2*guess))
    iterations = iterations + 1
print("Square root of",k,"is approximately",guess)
print("It squares to equal",guess*guess)
print("Iterations:",iterations)