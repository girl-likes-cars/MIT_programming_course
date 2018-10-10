# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 12:06:38 2018

@author: Maysa
"""

#need to find something close to square root of a number

#x = 123456 #the number we want
#epsilon = 0.01 #the error we are willing to live with
#step = epsilon**3 #not sure what this is yet
#numGuesses = 0
#ans = 0.0 #our starting point is zero
#
##as long as error exceeds error bound and is less than x, keep guessing
#while abs(ans**2 - x) >= epsilon and ans*ans <= x:
#    ans += step #add error-squared to our answer
#    numGuesses += 1
#print("numGuesses =",numGuesses)
#if abs(ans**2 - x) >= epsilon:
#    print("Sorry, my guess just isn't good enough.")
#else:
#    print(ans,"is close to square root of",x)

#bisection search method:
x = -27
epsilon = 0.01
numGuesses = 0
if x > 0:
    low = 0
    high = max(1.0, x)
    ans = (high + low)/2.0 #answer is an average of low and high
    while abs(ans**3 - x) >= epsilon: #while outside error bound
        print('low =',low, 'high =',high, 'ans =', ans) #print low, high and average
        numGuesses += 1
        if ans**3 < x:
            low = ans
        else:
            high = ans
        ans = (high + low)/2.0
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
    print('numGuesses = ', numGuesses)