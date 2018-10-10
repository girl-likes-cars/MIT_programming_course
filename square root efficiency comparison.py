# -*- coding: utf-8 -*-
"""
Created on Sun Jun 24 17:12:29 2018

@author: Maysa
"""

#FINDING SQUARE ROOTS: COMPARING EFFICIENCY OF 2 METHODS

#Bisection search method:
x = int(input("Give me a number whose square root you want to find! "))
epsilon = 0.01
numGuesses = 0
if x > 0:
    low = 0
    high = max(1.0, x)
    ans = (high + low)/2.0 #answer is an average of low and high
    while abs(ans**3 - x) >= epsilon: #while outside error bound
#        print('low =',low, 'high =',high, 'ans =', ans) #print low, high and average
        numGuesses += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print("\nBISECTION SEARCH RESULTS:")
    print("Square root is approximately",ans)
    print('numGuesses = ', numGuesses)
else:
    low = min(1.0, x)
    high = 0
    ans = (high + low)/2.0 #answer is an average of low and high
    while abs(ans**3 - x) >= epsilon: #while outside error bound
        print('low =',low, 'high =',high, 'ans =', ans) #print low, high and average
        numGuesses += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
    print("\nBISECTION SEARCH RESULTS:")
    print("Square root is approximately",ans)
    print('numGuesses = ', numGuesses)
    
#NEWTON'S METHOD
#Set the epsilon and the square root you want to find
#Pick a random starting point for your guess (let's say, guess/2)
guess = x/2.0
iterations = 0
while guess*guess - x >= epsilon:
    guess = guess - ((guess**2 - x)/(2*guess))
    iterations = iterations + 1
print("\n")
print("NEWTON'S RESULTS")
print("Square root of",x,"is approximately",guess)
print("It squares to equal",guess*guess)
print("Iterations:",iterations)

print("COMPARISON??")
if iterations < numGuesses:
    print("\nNewton is better than bisection!")
else:
    print("Something went wrong...Newton is worse??")