# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 19:26:38 2020

@author: Ethan
"""
def main():
    userChoice = 0
    while (userChoice != 8):
        userChoice = int(input("Enter which part you want to do: "))
        if (userChoice == 1):
            studentName = " "
            while (studentName != "0"): 
                studentName = str(input("Enter the first and last name of the student: "))
                if (studentName != "0"):                    
                    resultRoom = decideRoom(studentName,"last")
                    print("Last name: ",resultRoom[0])
                    print("Test Room: ",resultRoom[1])
                else:
                    print("End of Student Entry.")
        elif (userChoice == 2):
            filename = "C:/Users/Ethan/Documents/Python Scripts/LEarning_Python/Project 7/data.txt"
            nameFile(filename)
            
def decideRoom(enteredName,firstlast):
    sample = "abcdeABCDE1234567890"
    numsample = "1234567890"
    splitName = enteredName.split()
    firstRoom = "Room1"
    secondRoom = "Room2"
    if(firstlast == "last"):
        lastName = splitName[1]        
        searchSample = sample.find(lastName[0])
        if (searchSample != -1):
            return lastName,firstRoom
        else:
            return lastName,secondRoom
    elif (firstlast == "first"):
        firstName = splitName[0]
        searchSample = sample.find(firstName[0])
        if (searchSample != -1):
            numsearchsample = numsample.find(firstName[0])
            if (numsearchsample == -1):
                return firstName,firstRoom
            else:
                return "---","invalid"
        else:
            return firstName,secondRoom
    else:
        return "invalid","invalid"
def nameFile(userFile):
    openFile = open(userFile,'r')
    for line in openFile:        
        #getName = openFile.readline()        
        checkName = decideRoom(line,"first")
        print("First Name: ",checkName[0])
        print("Test Room: ",checkName[1])
        print("")
        
main()