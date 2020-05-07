# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 22:36:57 2020

@author: Ethan
"""
import random
import math
PI = math.pi
RADTO_DEGREES = 180/PI
numOfRand = 11
numQuestions = 5
exitNum = numQuestions + 1
MULT_NUM = 3
REPLACE_FACTOR = 5
REPLACE_NUM = 100
ANGLE_RANGE = 190
ANGLE_STEPS = 10
def main():
    userChoice = 0    
    while (userChoice != exitNum):        
        print("Welcome to project 5!")
        print("Enter which part you would like to run[1-",numQuestions,",",
                                                         exitNum,"to exit] ")
        userChoice = int(input("Selection: "))
        if(userChoice == 1):            
            readData()
        elif (userChoice == 2):
            editData()
        elif(userChoice == 3):
            enterScores()
        elif (userChoice == 4):
            writeData()
            p4()
        elif (userChoice == 5):
            p5()
        
    print("Goodbye!")
    
def writeData():    
    outfile = open('Example_File_1.txt','w')
    for num in range(1, numOfRand):
        myrandInt = random.randint(1,10)
        outfile.write(str(myrandInt)+"\n")        
    outfile.close()
def readData():
    writeData()    
    infile = open('Example_File_1.txt','r')
    currentNum = 0
    totalSum = 0
    count = 1
    for num in infile:
        currentNum = int(num)
        totalSum = totalSum + currentNum
        print("Number",count,"of list is: ",currentNum)        
        count += 1
    infile.close()
    averageofNum = totalSum/count    
    print("The total sum is: ",totalSum,"\nThe average is: ",averageofNum)
def editData():
    readData()
    editinfile = open('Example_File_1.txt','r')
    editoutfile = open('Example_File_2.txt','w')
    currentNum = 0
    newMultNum = 0
    count = 1
    for num in editinfile:
        currentNum = int(num)
        newMultNum = MULT_NUM * currentNum
        editoutfile.write(str(newMultNum)+ "\n")
        count += 1
    editinfile.close()
    print("The values have been edited.")
def enterScores():
    userContinue = ""
    userYear = 0
    numOfScores = 0
    scoreoutfile = open('Example_file_3.txt','w')
    while (userContinue != "e"):
        userYear = int(input("Enter a year: "))
        userScore = float(input("Enter a score: "))
        scoreoutfile.write(str(userYear))
        scoreoutfile.write(", ")
        scoreoutfile.write(str(userScore)+"\n")
        #scoreoutfile.append(str(userScore)+"/n")
        numOfScores += 1
        userContinue=str(input("Press any key to continue entering or 'e' to exit:"))
    scoreoutfile.close()
def p4():
    q4infile = open('Example_File_1.txt','r')
    q4outfile = open('Example_File_4.txt','w')
    currentNum = 0
    count = 1
    for num in q4infile:
        currentNum = int(num)
        if (currentNum < REPLACE_FACTOR):
            currentNum = REPLACE_NUM
        q4outfile.write(str(currentNum)+"\n")
        count += 1
    q4outfile.close()
    q4infile.close()
def p5():
    q5outfile = open('Example_File_5.txt','w')
    for angle in range(0,ANGLE_RANGE,ANGLE_STEPS):
        sinValue = math.sin(angle)*RADTO_DEGREES
        cosValue = math.cos(angle)*RADTO_DEGREES
        tanValue = math.tan(angle)*RADTO_DEGREES
        q5outfile.write("Angle: "+str(format(angle,'.2f'))+" ")
        #q5outfile.write()        
        q5outfile.write("sin: "+str(format(sinValue,'.2f'))+" ")
        q5outfile.write("cos: "+str(format(cosValue,'.2f'))+" ")
        q5outfile.write("tan: "+str(format(tanValue,'.2f'))+"\n")
        
main()
