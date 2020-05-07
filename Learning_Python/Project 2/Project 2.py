# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 02:59:19 2020

@author: Ethan
"""
userGrade = int
userChoice = int
rect1length = float
rect1width = float
rect2length = float
rect2width = float
userWeight = float
userNumber = float
numtoAdd = 25
pWorthVar = 10000
while (userChoice != 8):
    userChoice = int(input("Choose which program to run (1 - 7, 8 to quit)\n"))
    if (userChoice == 1):
        userGrade = int(input("Enter the grade: \n"))
        if (userGrade >= 80):
            print("The Letter grade is A \n")
        elif(userGrade >= 70):
            if(userGrade <= 79):
                print ("The Letter grade is B \n")
        elif (userGrade >=60):
            if(userGrade <= 69):
                print ("The Letter grade is C \n")
        elif (userGrade >= 50):
            if (userGrade <= 59):
                print ("The Lettergrade is D \n")
        elif (userGrade < 50):
            print ("The Letter grade is F \n")
    elif (userChoice == 2):
        rect1length = float(input("Enter length of first rectangle: \n"))
        rect1width = float (input ("Enter width of first rectangle: \n"))
        rect2length = float(input("Enter length of second rectangle: \n"))
        rect2width = float(input ("Enter width of second rectangle: \n"))
        rect1area = rect1length * rect1width
        rect2area = rect2length * rect2width
        if (rect1area > rect2area):
            print("Rectangle 1 is larger")
        elif (rect2area > rect1area):
            print ("Rectangle 2 is larger")
        else:
            print("They are equal")
    elif (userChoice == 3):
        userWeight = float(input("Enter the weight of the product\n"))
        if (userWeight > 10):
            print("The price is 3.8$\n")
        elif (userWeight > 6):
            if(userWeight <= 10):
                print("The price is 3.7$\n")
        elif(userWeight > 2):
            if(userWeight <=6):
                print("The price is 2.2$")
        else:
            print("The price is 1.1$")
    elif (userChoice == 4):
        userNumber = float(input("Enter a number between 12 and 35\n"))
        if (userNumber > 20):
            if(userNumber <=35):
                userNumber = userNumber + numtoAdd
                print ("The new number plus ", numtoAdd,"number is: ", userNumber ,"\n")
            else:
                print("That number is out of range.")
        elif(userNumber >=12):
            userNumber = userNumber * userNumber
            print("The new squared number is: ", userNumber)
        else:
            print("That number is out of range.")
    elif (userChoice == 5):
        userLength = float(input("Enter the length(from 5 to 700): \n"))
        if (userLength >= 5):
            if(userLength <= 700):
                userWidth = float(input("Enter the width(from 5 to 700): \n"))
                if(userWidth >= 5):
                    if(userWidth <= 700):
                        userArea = userLength * userWidth
                        userPerimeter = (userLength * 2) + (userWidth * 2)
                        print("The Area is: ", userArea, "\n")
                        print("The Perimeter is: ", userPerimeter, "\n")
                    else:
                        print("That value is not in range.")
                else:
                    print("That value is not in range.")
            else:
                print("That value is not in range.")
        else:
            print("That value is not in range.")
    elif (userChoice == 6):
        print("Sum of Squares")
        numupTo = 6
        squaredNums = (6**2)+(5**2)+(4**2)+(3**2)+(2**2)+(1**2)
        xMean = ((6+5+4+3+2+1)**2)/6
        sumofSquares = squaredNums - xMean
        print("Sum of squares is ", xMean)
    elif (userChoice == 7):
        iRate = float(input("Enter an interest rate between 1 and 2.5\n"))
        if (iRate > 2.5):
            print("That value is too large")
        elif (iRate <1):
            print("That value is too small")
        else:
            numYears = float(input("Enter the number of years between 10 and 15\n"))
            if (numYears > 15):
                print("That value is too large")
            elif(numYears <10):
                print("That value is too small")
            else:    
                for num in range (6):
                    pWorth = pWorthVar/(pow((1+(iRate/100)),numYears))
                    print("The Present Worth for ", pWorthVar, " is: ", pWorth)
                    pWorthVar = pWorthVar + 20000
            
        