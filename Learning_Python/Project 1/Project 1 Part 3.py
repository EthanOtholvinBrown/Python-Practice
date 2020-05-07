# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:44:23 2020
Excercises 1 Question 3
@author: Ethan
"""
#typical percentage of sales for determining profit
typPercent = 0.23
runorQuit = 'y'
while (runorQuit == 'y'):
    #take the projected sales from user
    projSales = float(input("Enter the total sales:"))
    #calculate the net profit
    netProfit = projSales*typPercent
    print("The projected profits are ", netProfit , "dollars")
    runorQuit = str(input("Type 'y' to run again, any other key to quit: "))