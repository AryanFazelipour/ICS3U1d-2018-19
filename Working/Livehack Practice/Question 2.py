#-------------------------------------------------------------------------------
# Name:		numberguess.py
#
# Purpose:	The guessing number game
#
# Author:	A. Fazelipour
#
# Created:	03/26/2019
#-------------------------------------------------------------------------------
print("*** Guess the Number ***")

print("Welcome to the guess the number game.")
print("You have 5 chances to guess the number between 0 and 100")

import random
num = 5
correct = False

count = 0
while count < 5:

    guess = int(input("Enter a number between 0 and 100: "))

    if guess > num:
        print("Too high, guess again")

    elif guess < num:
        print("Too low, guess again")
    else:
        correct = True

    count += 1
    if count == 5 and correct == False:
        print("Sorry, you've guessed incorrectly, the number is", num)
       break
if correct == True:
    print("Congratulations")
