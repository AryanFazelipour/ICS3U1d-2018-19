#-------------------------------------------------------------------------------
# Name:		markgroups.py
#
# Purpose:	Collects marks and prints scores
#
# Author:	A. Fazelipour
#
# Created:	03/26/2019
#-------------------------------------------------------------------------------
print("*** Mark Groups ***")

print("This program takes a collection of marks and counts how many outstanding scores (90-100), satisfactory scores (60-89), and the number of unsatisfactory scores (1-59).")

mark = int(input("Enter your mark from 0-100: "))
new_mark = input("Do you wish to enter another mark? (y/n): ")

mark_out = 0
mark_sat = 0
mark_unsat = 0

while new_mark == "y":
    mark = int(input("Enter your mark from 0-100: "))
    new_mark = input("Do you wish to enter another mark? (y/n): ")

    if mark >= 90 and mark <= 100:
        mark_out += 1

    elif mark >= 60 and mark <= 89:
        mark_sat += 1

    elif mark >= 1 and mark <= 59:
        mark_unsat += 1

    else:
        print("Error, put marks in range")

print("The number of outstanding marks is", mark_out)
print("The number of satisfactory marks is", mark_sat)
print("The number of unsatisfactory marks is", mark_unsat)

