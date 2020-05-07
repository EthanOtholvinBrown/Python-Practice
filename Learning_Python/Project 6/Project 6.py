# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:38:50 2020

@author: Ethan
"""
import math
import matplotlib
COMMISSION = 0.05
RVALUE = 8.314
NUM_OF_NUMBERS = 25
MAX_RAND = 100
MIN_RAND = 0
NUM_QUESTIONS = 25
MAX_DEGREES = 181
ANGLE_STEPS = 10
PI = math.pi
TODEGREES = 180/PI
import random
def main():
    userChoice = 0
    while (userChoice != 7):
        print("Enter which part you want to do[1-6, 7 to exit]:")
        userChoice = int(input())
        if (userChoice == 1):
            userList = getData()
            userProcess = processData(userList[0],userList[1],userList[2],userList[3])
            totalSales = userProcess[0]
            totalCommission = userProcess[1]
            print("Quarter 1 Sales: ",userList[0])
            print("Quarter 2 Sales: ",userList[1])
            print("Quarter 3 Sales: ",userList[2])
            print("Quarter 4 Sales: ",userList[3])
            print("Total Sales: ",totalSales)
            print("Sales Commission: ",totalCommission)
        elif (userChoice == 2):
            print("Under Construction.")
        elif (userChoice == 3):
            xValue = int(input("Enter a value of 'X'[0-100]: "))
            userList = generateData()
            print("Old List: ",userList)
            userResult = process(userList,xValue)
            
            print("New List: ",userResult[0])
            print("The Average of the old List: ",userResult[1])
            print("The Average of the new list: ",userResult[2])
        elif (userChoice == 4):
            score = 0
            compareLists = enterAnswers()
            for num in range (0,len(compareLists[0])):
                if (compareLists[0][num] == compareLists[1][num]):
                    score += 1
                else:
                    score += 0
            print("The score is: ",score)
            if (score > 17):
                print("It's a pass!")
            else:
                print("It's a fail :(")
        elif (userChoice == 5):
            userNum = int(input("Enter a value for its' prime values: "))
            userPrimeList = prime(userNum)
            print("List of primes: ")
            print(userPrimeList)
        elif (userChoice == 6):
            resultAngles = angle()
            numGreater = 0
            for num in range(0,len(resultAngles[1])):
                if(resultAngles[1][num] > 0.4):
                    numGreater += 1
            print("There are ",numGreater,"Larger than 0.4")
            plotangles(resultAngles[0],resultAngles[1],resultAngles[2],resultAngles[3])
def plotangles(anglePlot,sinPlot,cosPlot,tanPlot):
    matplotlib.pyplot.plot(anglePlot,sinPlot)
    matplotlib.pyplot.plot(anglePlot,cosPlot)
    matplotlib.pyplot.plot(anglePlot,tanPlot)
    matplotlib.pyplot.show()
def angle():
    mthListAngles =[[],[],[],[]]
    for angle in range(0,MAX_DEGREES,ANGLE_STEPS):
        mySin = math.sin(angle)*TODEGREES
        myCos = math.cos(angle)*TODEGREES
        myTan = math.tan(angle)*TODEGREES
        mthListAngles[0].append(angle)
        mthListAngles[1].append(mySin)
        mthListAngles[2].append(myCos)
        mthListAngles[3].append(myTan)
    return mthListAngles
def prime(x):
    primeList = []
    for primeIteration in range (1,x):
        isPrime = primeIteration%2
        if (isPrime != 0):
            primeList.append(primeIteration)
    return primeList
def enterAnswers():    
    iterationSol = 0
    solutions = []
    iterationAn = 0
    answers = []
    while (iterationSol <= NUM_QUESTIONS):
        randLetNum = random.randint(1,4)
        if (randLetNum == 1):
            solutions.append("A")
        elif (randLetNum == 2):
            solutions.append("B")
        elif (randLetNum == 3):
            solutions.append("C")
        else:
            solutions.append("D")
        iterationSol += 1
    while (iterationAn <= NUM_QUESTIONS):
        randLetNum = random.randint(1,4)
        if (randLetNum == 1):
            answers.append("A")
        elif (randLetNum == 2):
            answers.append("B")
        elif (randLetNum == 3):
            answers.append("C")
        else:
            answers.append("D")
        iterationAn += 1
    return solutions, answers
def generateData():
    mthNumList = []
    count = 0
    while (count <= NUM_OF_NUMBERS):
        myRand = random.randint(MIN_RAND,MAX_RAND)
        mthNumList.append(myRand)
        count += 1
    return mthNumList
def process(mthGeneratedList, userX):
    processCountOld = 0
    indexOld = 0
    sumOfListOld = 0
    sumOfListNew = 0
    processCountNew = 0
    indexNew = 0
    newList = []
    for num in range(0,len(mthGeneratedList)):
        #print("Index is: ",indexOld)        
        if (mthGeneratedList[num] < userX):
            mthGeneratedList[num] = mthGeneratedList[num] * 2
            newList.append(mthGeneratedList[num])
        else:
            newList.append(mthGeneratedList[num])
        sumOfListOld = sumOfListOld + mthGeneratedList[num]
        processCountOld += 1
        indexOld += 1
    for num2 in range(0,len(newList)):
        sumOfListNew = sumOfListNew + newList[num2]
        processCountNew += 1
        indexNew += 1
    listAverageOld = sumOfListOld/len(mthGeneratedList)
    listAverageNew = sumOfListNew/len(newList)
    return newList,listAverageOld,listAverageNew
def processData(list1, list2, list3, list4):
    sumlist1 = 0
    sumlist2 = 0
    sumlist3 = 0
    sumlist4 = 0
    for numinlist1 in range (0, len(list1)):
        sumlist1 = sumlist1 + list1[numinlist1]
    for numinlist2 in range(0, len(list2)):
        sumlist2 = sumlist2 + list2[numinlist2]
    for numinlist3 in range(0, len(list3)):
        sumlist3 = sumlist3 + list3[numinlist3]
    for numinlist4 in range(0,len(list4)):
        sumlist4 = sumlist4 + list4[numinlist4]
    totalSumMethod = sumlist1 + sumlist2 + sumlist3  + sumlist4
    salesCommissionMethod = totalSumMethod * COMMISSION
    return totalSumMethod, salesCommissionMethod
def getData():
    index = 0           
    getSales = 0   
    salesList1 = []
    while(getSales != "q"):
        getSales = str(input("Input the sales for quarter 1 ['q' to stop]: "))
        if (getSales != "q"):
            getSales = float(getSales)
            salesList1.append(getSales)
            index += 1
        else:
            print("End of quarter") 
    getSales = 0        
    salesList2 = []
    while(getSales != "q"):
        getSales = str(input("Input the sales for quarter 2 ['q' to stop]: "))
        if (getSales != "q"):
            getSales = float(getSales)
            salesList2.append(getSales)
            index += 1
        else:
            print("End of quarter") 
    getSales = 0        
    salesList3 = []
    while(getSales != "q"):
        getSales = str(input("Input the sales for quarter 3 ['q' to stop]: "))
        if (getSales != "q"):
            getSales = float(getSales)
            salesList3.append(getSales)
            index += 1
        else:
            print("End of quarter")
    getSales = 0        
    salesList4 = []
    while(getSales != "q"):
        getSales = str(input("Input the sales for quarter 4 ['q' to stop]: "))
        if (getSales != "q"):
            getSales = float(getSales)
            salesList4.append(getSales)
            index += 1
        else:
            print("End of quarter")
    return salesList1, salesList2, salesList3, salesList4
main()