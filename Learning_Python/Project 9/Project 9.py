# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:24:53 2020

@author: Ethan
"""
import pet
import energy
import random
import rockpaperscissor
def main():
    userChoice = 0
    while(userChoice != 4):
        userChoice = int(input("Enter a question to run: "))
        if(userChoice == 1):
            print("Enter information about your pet.")
            name = str(input("Enter its name: "))
            aType = str(input("Enter what type of animal it is: "))
            age = int(input("Enter its age: "))
            info = pet.Pet(name,aType,age)
            info.set_name()
            info.set_animal_type()
            info.set_age()
            print("name = ",info.get_name())
            print("type = ",info.get_animal_type())
            print("age = ",info.get_age())
        elif(userChoice == 2):
            print("This section will compare two energy values.")
            results = compare()
            print("Energy 1: ",format(results[0],'.2f'))
            print("Energy 2: ",format(results[1],'.2f'))
            print("Winner: ", results[2])
        elif(userChoice == 3):
            print("Let's play Rock, Paper, Scissors~!")            
            gameplay = rockpaperscissor.RockPaperScissor()
            computerWins = 0
            userWins = 0
            ties = 0
            for n in range(1,6):
                print("Game ",n,":")
                user = str(input("Pick your choice[type 'rock','paper', or 'scissors']: "))
                gameplay.set_rpsValue()
                computer = gameplay.get_rpsValue()
                print("Computer plays: ",computer)
                if(user == 'rock' and computer == 'paper'):
                    print("Computer wins this round!")
                    computerWins +=1
                elif(user == 'rock' and computer == 'scissors'):
                    print ("You win this round!")
                    userWins +=1
                elif(user == 'paper' and computer == 'rock'):
                    print("You win this round!")
                    userWins +=1
                elif (user == 'paper' and computer == 'scissors'):
                    print("Computer wins this round!")
                    computerWins +=1
                elif (user == 'scissors' and computer == 'rock'):
                    print("Computer wins this round!")
                    computerWins +=1
                elif(user == 'scissors' and computer == 'paper'):
                    print("You win this round!")
                    userWins +=1
                elif(user == computer):
                    print("It's a tie!")
                    ties += 1
                else:
                    print("That is not a valid answer. Enter again.")                    
            print("Final Score")
            print("You: ",userWins)
            print("Computer: ",computerWins)
            print("Ties: ",ties)
            if (userWins > computerWins):
                print("You win!")
            elif(computerWins > userWins):
                print("Computer wins!")
            else:
                print("It's a tie!")
def createObjects():
    m = random.randint(1,100)
    v = random.randint(1,100)
    h = random.randint(1,100)
    values = energy.Energy(m,v,h)
    values.set_ke()
    values.set_pe()
    ke = values.get_ke()
    pe = values.get_pe()
    return ke, pe
def compare():
    myobjects = createObjects()
    energy1 = myobjects[0]
    energy2 = myobjects[1]
    if (energy1 > energy2):
        return energy1,energy2,"Energy 1"
    else:
        return energy1,energy2,"Energy 2"
main()