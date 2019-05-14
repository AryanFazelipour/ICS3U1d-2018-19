#-------------------------------------------------------------------------------
# Name:		ouncesgrams.py
#
# Purpose:	A progam that converts ounces to grams from 1 to 15
#
# Author:	A. Fazelipour
#
# Created:	03/26/2019
#-------------------------------------------------------------------------------

print("**** Ounces to Grams Converter ****")

print("This program will print out a titled table that can be used to covert ounces to grams, for values from 1 to 15 ounces (1 ounce = 28.35 grams)")

# Table header
print("{0:>15} {01:>20}".format("Ounces", "Grams"))

#Convert Ounces to pounds
total = 1
for ounces in range(16):
    grams = round(ounces * 28.35, 2)
    print("{0:15} {01:>22}".format(ounces, grams))
