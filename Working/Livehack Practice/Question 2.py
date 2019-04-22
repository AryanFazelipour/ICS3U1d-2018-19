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
guess = int(input("Enter a number between 0 and 100: "))

count = 0
while guess != num:

    if guess > num:
        print("Too high, guess again")

    elif guess < num:
        print("Too low, guess again")

    guess = int(input("Enter a number between 0 and 100: "))

    count += 1
    if count == 4:
        print("Sorry, you've guessed incorrectly, the number is", num)
        break
else:
    print("Congratulations")
