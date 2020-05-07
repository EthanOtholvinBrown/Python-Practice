# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 17:51:02 2020
Excercise 1 Question 4
@author: Ethan
"""
salesTax = .06
runorQuit = 'y'
while (runorQuit == 'y'):
    item1 = float(input("Enter price of first item: "))
    item2 = float(input("Enter price of second item: "))
    item3 = float(input("Enter price of third item: "))
    item4 = float(input("Enter price of fourth item: "))
    item5 = float(input("Enter price of fifth item: "))
    totalNoTax = item1+item2+item3+item4+item5
    totalWithTax= (totalNoTax*salesTax)+totalNoTax
    print("Subtotal: ", totalNoTax,
          "Tax: ", salesTax,
          "Total: ", totalWithTax)
    print(" ")
    runorQuit = str(input("Enter 'y' to run again or any other key to quit: "))