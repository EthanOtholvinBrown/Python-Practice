# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:33:22 2020

@author: Ethan
"""
#constants for question 1
NUMOF_SQUARES = int
userChoice = int
SUM = 0
#constants for question 2
INTERESTINTERVAL_1 = 1
INTERESTINTERVAL_2 = 2.5
YEARSINTERVAL_1 = 10
YEARSINTERVAL_2 = 15
FUTVAL_1 = 10000
FUTVAL_2 = 100000
INCREMENT = 20000
LIM_LOW = 0
#constants for question 4
Q4USERRANGE_LOW = 15
Q4USERRANGE_HIGH = 30
#constants for question 5
Q5USERRANGE_LOW = 0
Q5USERRANGE_HIGH = 7
while (userChoice != 8):
    userChoice = int(input("Enter which program to run [1-7, 8 to exit]\n"))
    if (userChoice == 1):
        NUMOF_SQUARES = int(input("Enter the number of sum of squares to find: \n"))
        for num in range (1,NUMOF_SQUARES+1):
            numSquare = pow(num,2)
            SUM = SUM + numSquare
            print("The sum of squares of ", num ," is ", SUM, "\n")
    elif (userChoice == 2):
        rate = float(input("Enter the interest rate [1-2.5]\n"))
        if (rate < INTERESTINTERVAL_1 or rate > INTERESTINTERVAL_2):
            print("That value is out of range.")
        else:
            numYears = int(input("Enter the number of years[10-15]\n"))
            if (numYears < YEARSINTERVAL_1 or numYears > YEARSINTERVAL_2):
                print("That value is out of range.")
            else:
                for num in range(FUTVAL_1,FUTVAL_2,INCREMENT):
                    presentValue = num/pow((1+rate/100),numYears)
                    print("Present value for year ", num," is ", format(presentValue,'.2f'), "\n")
                    
    elif (userChoice == 3):
        userCel = int(input("Enter the celsius value[min 0, no decimals]: \n"))
        if (userCel < 0 ):
            print("That value is out of range.")
        else:
            print("----------------------")
            print("Celsius \t Fahrenheit \n")
            for num in range(LIM_LOW, userCel+1): #added a +1 to bring it into right range
                userFahr = ((9/5)*num) + 32
                print(num,"\t \t",format(userFahr,'.1f'))
    elif (userChoice == 4):
        print("Enter a celsius value between", Q4USERRANGE_LOW, " and ", Q4USERRANGE_HIGH)
        userCel2 = int(input())
        while (userCel2 < Q4USERRANGE_LOW or userCel2 >Q4USERRANGE_HIGH):
            print("not in range, enter a valid number [",Q4USERRANGE_LOW,"-",Q4USERRANGE_HIGH,"]:")
            userCel2 = int(input())
        userFahr2 = ((9/5)*userCel2) + 32
        print (userCel2,"degrees celsius in Fahrenheit is: ",format(userFahr2,'.2f'))
    elif (userChoice == 5):
        print("Enter a value for N [",Q5USERRANGE_LOW,"-",Q5USERRANGE_HIGH,"]")
        userN = int(input())
        while (userN < Q5USERRANGE_LOW or userN > Q5USERRANGE_HIGH):
            print("Not in range, enter a valid number [",Q5USERRANGE_LOW,"-",Q5USERRANGE_HIGH,"]")
            userN = int(input())
        resultFact = 1
        for num in range(Q5USERRANGE_LOW+1,userN+1): #added a +1 to bring it into required range
            resultFact = resultFact * num              
        print("The factorial of ",userN," is ",resultFact,"\n")
    elif (userChoice == 6):
        numStars = int(input("Enter the number of stars you want: \n"))
        for num in range (1, numStars+1):
            for num2 in range (num, numStars+1):
                print("*", end='')
            print("\n")
    elif (userChoice == 7):
        userNum = int(input("Enter a positive number (negative to end entry)\n"))
        addedNums = 0
        while (userNum >=0):
            addedNums = addedNums + userNum
            userNum = int(input("Enter a positive number (negative to end entry)\n"))
        print("The final sum is: ",addedNums)