# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:41:23 2018

@author: Maysa
"""

#user inputs
starting_salary = float(input("Enter your starting salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))
semi_annual_raise = float(input("Enter your semi-annual raise as a decimal percentage: "))

#calculated variables
month = 0
portion_down_payment = float((1/4)*total_cost)
current_savings = 0

#OUTER LOOP: as long as savings aren't sufficient, keep saving
while current_savings < portion_down_payment:
    month = month + 1
    number_of_raises = month//6
    adjusted_salary = float(starting_salary*((1 + semi_annual_raise)**number_of_raises))
    contribution_for_the_month = float((adjusted_salary*portion_saved)/12)
    current_savings = float((301/300)*current_savings + contribution_for_the_month)
print("\nNumber of months: ",month)
print(current_savings)