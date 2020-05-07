# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 13:34:08 2020

@author: Ethan
"""
import math
import random
def main():
    userChoice = 0
    while (userChoice != 6):
        print("Press 6 to exit.")
        userChoice = int(input("Enter which part you want to do: "))
        if(userChoice == 1):            
            valueDictionary = getInputs()
            key = "null"
            while (key != "quit"):
                print("Type 'quit' to exit")
                print("Enter which calculation you want to see: ")
                key = str(input())
                if (key != "quit"):
                    print("m = ",valueDictionary[key][0])
                    print ("v = ",valueDictionary[key][1])
                    print("k = ",valueDictionary[key][2])
                else:
                    print("Returning to main menu...")
        elif (userChoice == 2):   
            quizResults = quiz()
            if (quizResults[0] == "Pass"):
                print("You passed!")
                print("Correct answers: ",quizResults[1])
            else:
                print("You failed.")
                print("Correct answers: ",quizResults[1])
        
        
            
            
def quiz():  
    print("Enter the two tables you want a quiz for.")
    firstT = int(input("Table 1: "))
    secondT = int(input("Table 2: "))
    myT = createTables(firstT,secondT)
    correctAnswer = 0      
    result = "neutral"
    for quizNum in range(1,6):
        myRan1 = random.randint(1,20)
        print(myT[myRan1][0],"x",myT[myRan1][1],"= ")
        userAnswer = int(input())
        if(userAnswer == myT[myRan1][2]):
            correctAnswer += 1
        else:
            correctAnswer += 0
    if (correctAnswer > 2):
        result = "Pass"
        return result,correctAnswer,userAnswer
    else:
        result = "Fail"
        return result,correctAnswer,userAnswer
def createTables(t1,t2):    
    table = {}    
    for num in range(1,21):       
        if (num <= 10):
            valT1 = t1 * num                
            table[num] = [t1,num,valT1]
        else:
            count1 = 20 - num                           
            valT2 = t2 * count1
            table[num] = [t2,count1,valT2]
    
    return table
def getInputs():
    subIn = {}
    userKey = "null"
    while (userKey != "quit"):
        print ("Type 'quit' to exit")
        userKey = str(input("Enter what you want the set of values to be called: "))
        if(userKey != "quit"):            
            m = int(input("Enter an 'm' value: "))
            v = int(input("Enter a 'v' value: "))
            k = calculateK(m,v)
            subIn[userKey] = [m,v,k]            
        else:
            print("Loading output...")
    return subIn
    
def calculateK(userM,userV):
    userK = 0.5*(math.pow((userM * userV),2))
    return userK
main()