"""
Kevin Li
420-LCU Computer Programming, Section 1
Wednesday, Febuary 21st
S. Hilal, Instructor
Assignment 1
"""

import random
number = int(input("please think of any number: "))
x = number - 20
y = number + 20
n = random.randint(x,y)
winning = False

while winning == False:
    print(n)
    print("Enter 'h' if my guess is too high, 'l' if too low, or 'c' if I am correct")
    rangeAnswer = input()

    if rangeAnswer == "h":
        y = n - 1
        n = random.randin(x,y)
        print(n)

    elif rangeAnswer == "l":
        x = n + 1
        n = random.randint(x,y)
        print(n)

    if rangeAnswer == "c":
        print("Game over, your secret nubmer was:",n)
        winning == True
        break

