"""
Kevin Li
420-LCU Computer Programming, Section 1
Wednesday, Febuary 21st
S. Hilal, Instructor
Assignment 1
"""

import random #we use this command in order for the program to generate random numbers

number = int(input("please think of any number: "))

x = 0 #we set the minimum value to be 0 in order to not have negative numbers
y = number + 20 #we set the maximum guess value to be 20 more than the number in order to prevent the guess generated by the computer to be extremely high
#I set these variables like this so that the player can use any numbers and not be restricted to a certain range

keywordsHigh = ["high", "big","large", "great"]
keywordsLow = ["low", "small",  "tiny", "miniscule", "short", "little", "petite"]
keywordsCorrect = ["right", "correct", "got it", "did it", "congrats", "congratulation", "you won", "I lost", "you win", "I lose"]
n = random.randint(x,y) #this was used to specify the range of the randomly generated number

winning = False 

while winning == False:
    print(n) #show the player the computer's guess
    print("Please specify if my guess is too high or too low or if I guessed it correctly")
    rangeAnswer = input()
    lowerRangeAnswer = rangeAnswer.lower()
    if any(i in rangeAnswer for i in keywordsHigh):
        y = n - 1 #this is so that the computer will not guess a number that is higher than the number that it just guessed
        n = random.randint(x,y) #this is used to specify the range of the randomly generated number with the new range
      

    elif any(i in rangeAnswer for i in keywordsLow):
        x = n + 1 #this is so hat the computer will not guess a number that is lower than the number that it just guessed
        n = random.randint(x,y) #this is used to specify the range of the randomly generated number with the new range
       

    if any(i in rangeAnswer for i in keywordsCorrect):
        print("Game over, your secret nubmer was:",n)
        winning == True
        break

