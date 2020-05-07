# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 18:01:24 2020
Excercise 1 Question 5
@author: Ethan
"""
runorQuit = 'y'
while (runorQuit == 'y'):
    time5 = 5
    time8 = 8
    time12 = 12
    carSpeed = float(input("Enter speed of the car (in miles): "))
    dist5 = carSpeed * time5
    dist8 = carSpeed * time8
    dist12 = carSpeed * time12
    print("The car will travel ", dist5," miles in 5 hours.")
    print("The car will travel ", dist8 ," miles in 8 hours.")
    print("The car will travel ", dist12," miles in 12 hours.")
    runorQuit = str(input("Press 'y' to run again, any other key to quit: "))