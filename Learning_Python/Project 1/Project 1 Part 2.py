# -*- coding: utf-8 -*-
"""
Practice Excercises 1 Question 2
Ethan Brown

"""
#decide which part of the question to run
decision = str
numofMarks = 2
multiplier = 10
pie = 3.14
rate = 1.5
while (decision != 'q'):
    print(" ")
    print("a- averageCalc, b-Mileage, c- multiplication by 10, d-measurements",
      ", e-pay program, f-ocean level, q - quit")
    decision = str(input("Choice: "))
    if (decision == 'a'):
        score1 = float(input("Input first mark: "))
        score2 = float(input("Input second mark: "))
        average = (score1+score2)/numofMarks
        print ("The Average is: ", average)
        print(" ")
    if (decision == 'b'):
        distance1 = float(input("Input distance in KM: "))
        litres1 = float(input("Input litres of gas: "))
        mileage = distance1/litres1
        print("The mileage is: ", mileage)
        print(" ")
    if (decision == 'c'):
        userNum = float(input("Input the number to multiply: "))
        multNum = userNum * multiplier
        print("The result is: ", multNum)
        print(" ")
    if (decision == 'd'):        
        radius = float(input("Input the radius: "))
        diameter = radius * 2
        circumference = diameter * pie
        area  = pie * radius * radius
        print("Diameter: ", diameter,
              "Circumference: ", circumference,
              "Area: ", area)
        print(" ")
    if (decision == 'e'):
        payRate = float(input("Enter the pay rate: "))
        hoursWorked = float(input("Enter the hours worked: "))
        percentage = float(input("Enter the percentage of gross salary: "))
        grossPay = payRate * hoursWorked
        withholdAm = grossPay * (percentage/100)
        netPay = grossPay - withholdAm
        print("The Net Pay is: ", netPay)
        print(" ")
    if (decision == 'f'):        
        currentLevel = float(input("Enter current sea level(mm): "))
        after3 = currentLevel + rate*3
        after5 = currentLevel + rate*5
        after10 = currentLevel + rate*10
        print("After 3 years: ", after3,
              "After 5 years: ", after5,
              "After 10 years: ", after10)
        print(" ")
    