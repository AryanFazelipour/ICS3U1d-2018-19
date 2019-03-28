#-------------------------------------------------------------------------------
# Name:		TripChecker.py
#
# Purpose:	Given average and earnings, determine if a trip to Europe, California or nowhere will occur
#
# Author:	A. Fazelipour
#
# Created:	03/26/2019
#-------------------------------------------------------------------------------

# Get average and earnings
average = int(input("Enter average here: "))
earnings = int(input("Enter earnings here: "))

# Determine if I have requirements to go on vacation

if average >= 80 and earnings >= 500:
    print("You can go to Europe")



elif average >= 80:
    print("You can go to California")

else:
    print("Staying home")