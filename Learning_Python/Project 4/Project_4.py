# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 14:51:25 2020

@author: Ethan
"""
import math
imaginary = "imaginary"
MY_POWER = 2
MY_POWER2 = 2#power used for question 7
PI = 3.14
RADTO_DEGREES = 180/PI #the value to convert RAD to DEGREES
UVALUE_MIN = -3
UVALUE_MAX = 3
AVALUE_MIN = 0
AVALUE_MAX = 12
def main():
    userChoice = 0
    print("Welcome to Project 4!")
    print("")    
    while (userChoice != 8):        
        userChoice = int(input("Enter which part you would like to run[1-7, 8 to quit]: \n"))
        if (userChoice == 1):
            print("This part will be calculating Sin, Cos or Tan of a value.")
            xValue = float(input("Enter the 'x' value: \n"))           
            result = Question1(xValue)
            print("When calculating ",result[0]," the degrees are: ",format(result[1],'.2f'))
        elif (userChoice == 2):
            print("Enter the 3 numbers you would like to compare: \n")
            comp1 = int(input("Number 1: "))
            comp2 = int(input("Number 2: "))
            comp3 = int(input("Number 3: "))
            comparison = Question2(comp1, comp2, comp3)
            if (comparison[1] != comparison[3]):
                print("The ",comparison[0]," is ",comparison[1])
                print("\n The ",comparison[2]," is ",comparison[3])
            
        elif (userChoice == 3):
            userWidth = float(input("Enter the width[1-10]: \n"))
            userLength = float(input("Enter the length[1-10]: \n"))
            userArea = rect(userWidth,userLength)
            print("The area is:",userArea)
        elif (userChoice == 4):
            userA = float(input("Enter the 'A' value: "))
            userB = float(input("Enter the 'B' value: "))
            userC = float(input("Enter the 'C' value: "))
            resultRoots = rootTerms(userA,userB,userC)
            if (resultRoots[0] != imaginary):
                print("Root 1:",format(resultRoots[0],'.2f')
                ,"\nRoot 2:",format(resultRoots[1],'.2f'))
            else:
                print("There are no real roots.")
        elif (userChoice == 5):
            x1 = float(input("Enter coordinate 'X1': "))
            while(x1 > 0):
                x1 = float(input("Enter within range of quadrant 2 or 3: "))
            y1 = float(input("Enter coordinate 'Y1': "))
            x2 = float(input("Enter coordinate 'X2': "))
            while (x2 < 0):
                x2 = float(input("Enter within range of quadrant 1 or 4: "))
            y2 = float(input("Enter coordinate 'Y2': "))
            resultDistance = format(distance(x1,y1,x2,y2),'.2f')
            resultAngle = format(angle(x1,y1,x2,y2),'.3f')
            print("The distance is: ",resultDistance
                  ,"\nThe angle is: ",resultAngle," degrees")
        elif (userChoice == 6):
            resultList = func_getData()
            numInList = len(resultList)
            for num in range (0,numInList):
                print(resultList[num],"\n")
        elif (userChoice == 7):
            print("Enter the 'u' value between [",UVALUE_MIN,"< u <",UVALUE_MAX,"]")
            userUValue = float(input())
            print("Enter the 'a' value between [",AVALUE_MIN,"< a <",AVALUE_MAX,"]")
            userAValue = float(input())
            calcResult = calculateDistance(userUValue,userAValue)
            if (calcResult[0] != imaginary):
                print("'u' value entered: ",calcResult[1])
                print("'a' value entered: ",calcResult[2])
                print("Result distance is: ",calcResult[0])
            else:
                print("The result is imaginary.")
        else:
            print("Good Bye!")
def Question1(x):
    
    sinValue = math.sin(x)*RADTO_DEGREES
    cosValue = math.cos(x)*RADTO_DEGREES
    tanValue = math.tan(x)*RADTO_DEGREES
    userangleChoice = str(input("Do you want sin, cos or tan?: \n"))
    if (userangleChoice == "sin"):
        return "sin", sinValue
    elif (userangleChoice == "cos"):
        return "cos", cosValue
    elif (userangleChoice == "tan"):
        return "tan", tanValue
def Question2(num1,num2,num3):
    high = "highest"
    low = "lowest"
    null = ""
    if (num1>num2 and num1>num3):
        if (num2 > num3):
            return high,num1,low,num3
        else:
            return high,num1,low,num2
    elif (num2>num1 and num2>num3):
        if (num1>num3):
            return high, num2,low, num3
        else:
            return high, num2,low, num1
    elif (num3>num1 and num3>num2):
        if(num1>num2):
            return high, num3,low, num2
        else:
            return high, num3,low, num1
    else:
        print("\nThey are all equal.")
        return null,num1,null,num2
def rect(firstWidth, firstLength):
    correctValues = getValues(firstWidth,firstLength)
    area = correctValues[0] * correctValues[1]
    return area
def getValues(width, length):
    if (width < 1 or width > 10):
        while (width < 1 or width > 10):
            width = int(input("Please enter a width within range [1-10]\n"))
        
        if (length < 1 or length >10):
            while (length < 1 or length > 10):
                length = int(input("Please enter a length within range [1-10]\n"))
            return width,length        
        else:
            return width,length
        return width,length
    else:
        return width,length    
def rootTerms(a,b,c):
    checkFor = rootCheck(a,b,c)
    if (checkFor[0] != imaginary):
        firstRoot = checkFor[0]/(2*a)
        secondRoot = checkFor[1]/(2*a)
        return firstRoot, secondRoot #returns first root at positon [1], second root at position [2]
    else:
        return checkFor[0],""
def rootCheck(term1,term2,term3):
    squareRoot = term2 - (4*term1*term3)
    if (squareRoot <= 0):
        return imaginary,""
    else:
        topFormula1 = -term2 + squareRoot
        topFormula2 = -term2 - squareRoot
        if(topFormula1 == topFormula2):
            print("The terms are equal.")
            return topFormula1,topFormula2
        else:
            print("There are multiple terms.")
            return topFormula1,topFormula2   
def distance(coord1,coord2,coord3,coord4):
    distance = math.sqrt(math.pow((coord3-coord1),MY_POWER) + math.pow((coord4-coord2),MY_POWER))
    return distance
def angle (coord1,coord2,coord3,coord4):
    thetaRad = math.atan((coord4-coord2)/(coord3-coord1))
    thetaDegrees = thetaRad*RADTO_DEGREES
    return thetaDegrees
def func_getData():
    userEntry = "0"
    userList = []
    while (userEntry == "0"):
        userName = str(input("Enter a name: "))
        userGender = str(input("Enter their gender: "))
        userAge = int(input("Enter their age: "))
        userWage = float(input("Enter their wage: "))
        userData = [userName,userGender,userAge,userWage]
        userList.append(userData)
        userEntry = str(input("['0' to enter another, any other key to exit]\n"))
    return userList
def getInput(uValue,aValue):    
    if (uValue < UVALUE_MIN or uValue > UVALUE_MAX):
        while (uValue < UVALUE_MIN or uValue > UVALUE_MAX):
            uValue = float (input("Please enter a value within range[",UVALUE_MIN," < u <",UVALUE_MAX,"]:\n"))
        if (aValue < AVALUE_MIN or aValue > AVALUE_MAX):
            while(aValue < AVALUE_MIN or aValue > AVALUE_MAX):
                aValue = float(input("Please enter a value within range [",AVALUE_MIN,"< a <",AVALUE_MAX,"]:\n"))
            return uValue,aValue
        return uValue,aValue
    else:
        return uValue,aValue
def calculateDistance(userU,userA):
    cValue = 0 #the 'c' in this quadratic equation has no value
    checkedValues = getInput(userU,userA)
    correctU = checkedValues[0]
    correctA = checkedValues[1]
    quadAValue = correctA * 0.5 #0.5 is a constant from the formula
    calcDisplacement = rootTerms(quadAValue,correctU,cValue)    
    if(calcDisplacement[0] != imaginary):
        quadValA = math.pow(calcDisplacement[0],MY_POWER2)*.5
        quadValB = calcDisplacement[1]*correctU
        resultDisplacement = quadValA + quadValB
        return resultDisplacement,correctU,correctA
    else:
        return imaginary,correctU,correctA
        
    
main()
    
    
    
        