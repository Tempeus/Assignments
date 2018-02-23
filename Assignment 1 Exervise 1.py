"""
Kevin Li
420-LCU Computer Programming, Section 1
Wednesday, Febuary 21st
S. Hilal, Instructor
Assignment 1
"""

import random #we use this command in order for the program to generate random numbers

number = int(input("Please think of a number from 1 to 100: "))

x = 0 
y = 100


#I made a keyword list so the program will understand if it's guess is too high or too low or if they won, so he player can write phrases instead of writing a single word.
keywordsHigh = ["high", "big", "large", "great", "huge", "massive", "immense", "gigantic", "enormous", "tremendous"]
keywordsLow = ["low", "small",  "tiny", "miniscule", "short", "little", "petite"]
keywordsCorrect = ["right", "correct", "got it", "did it", "congrat", "you won", "I lost", "you win", "I lose", "perfect", "good"]

n = (x + y)//2

winning = False 

while winning == False:
    print(n) #show the player the computer's guess
    print("Please specify if my guess is too high or too low or if I guessed it correctly")
    rangeAnswer = input()
    lowerRangeAnswer = rangeAnswer.lower() #this is so that it will lower case the input that the player inserted in order to properly compare with the keyword list
    if any(i in lowerRangeAnswer for i in keywordsHigh): #This is to see if there is a keyword in the input that the player inserted
        y = n - 1 #this is so that the computer will not guess a number that is higher than the number that it just guessed
        n = (x + y)//2 
      

    elif any(i in lowerRangeAnswer for i in keywordsLow):
        x = n + 1 #this is so hat the computer will not guess a number that is lower than the number that it just guessed
        n = (x + y)//2 
       

    if any(i in lowerRangeAnswer for i in keywordsCorrect):
        print("Game over, your secret nubmer was:",n)
        winning == True
        break

