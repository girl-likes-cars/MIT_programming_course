# -*- coding: utf-8 -*-
"""
Created on Fri Jun  8 15:41:23 2018

@author: Maysa
"""

#user inputs
annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost = float(input("Enter the cost of your dream home: "))

#calculated variables
monthly_salary = float(annual_salary/12)
monthly_savings = float(monthly_salary*portion_saved)
portion_down_payment = float((1/4)*total_cost)
current_savings = 0
month = 0

while current_savings < portion_down_payment:
    current_savings = (301/300)*current_savings + monthly_savings
    month = month + 1
print("\nNumber of months: ",month)