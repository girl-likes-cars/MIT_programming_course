# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:41:23 2018

@author: Maysa
"""

#user inputs
starting_salary = float(input("Enter your starting salary: "))
low = 0
high = 1.0
saving_rate = (low + high)/2  # find middle point between low and high
semi_annual_raise = 0.07
numGuesses = 0 

# calculate starting point for savings given above saving rate (of 0.5)
month = 0
portion_down_payment = 250000
current_savings = 0   
while month <= 36:
    month = month + 1
    number_of_raises = month//6
    adjusted_salary = float(starting_salary*((1 + semi_annual_raise)**number_of_raises))
    contribution_for_the_month = float((adjusted_salary*saving_rate)/12)
    current_savings = float((301/300)*current_savings + contribution_for_the_month)

# WHILE LOOP: as long as savings aren't close enought to down payment amount, adjust saving rate
while abs(current_savings - portion_down_payment) > 100 and saving_rate < 1.0:
    # if savings are too low, increase saving rate and recalculate savings
    if current_savings < portion_down_payment:
        numGuesses += 1
        low = saving_rate
        saving_rate = float((low + high)/2)
        current_savings = 0
        month = 0
        while month <= 36:
            month = month + 1
            number_of_raises = month//6
            adjusted_salary = float(starting_salary*((1 + semi_annual_raise)**number_of_raises))
            contribution_for_the_month = float((adjusted_salary*saving_rate)/12)
            current_savings = float((301/300)*current_savings + contribution_for_the_month)
    # otherwise savings must be too high, so lower saving rate and recalculate savings
    else: 
        numGuesses += 1
        high = saving_rate
        saving_rate = float((low + high)/2)
        current_savings = 0
        month = 0
        while month <= 36:
            month = month + 1
            number_of_raises = month//6
            adjusted_salary = float(starting_salary*((1 + semi_annual_raise)**number_of_raises))
            contribution_for_the_month = float((adjusted_salary*saving_rate)/12)
            current_savings = float((301/300)*current_savings + contribution_for_the_month)
# if savings rate has reached or exceeded 100% saving, this means you just don't have enough money
if abs(current_savings - portion_down_payment) > 100 and saving_rate >= 1.000:
    print("Sorry, you just don't have enough money to do this.")
# otherwise you've reached your desired down payment, so print the resulting saving rate
else:
    print("\nSaving rate in decimal: ",round(saving_rate, 4))
    print("\nSteps in bisection search: ",numGuesses)
