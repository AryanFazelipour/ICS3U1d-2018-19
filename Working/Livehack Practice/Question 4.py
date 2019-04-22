#-------------------------------------------------------------------------------
# Name:		compoundInvesting.py
#
# Purpose:  Compound Interest Calculator
#
# Author:	A. Fazelipour
#
# Created:	03/26/2019
#-------------------------------------------------------------------------------
print("*** Compound Interest Calculator ***")

yearly_invest = int(input("\nEnter the yearly investment: "))
interest_rate = float(input("Enter the interest rate(%): "))
rate = interest_rate / 100
years = int(input("Please enter the number of years for the investment: "))

# Table header
print("\n{0:<15} {1:<30} {2:<25} {3:}".format("Year", "Amount in Account", "Interest Earned", "Total"))
i = 0
total = 0
while i < years:
    i += 1
    account = yearly_invest + total
    interest_earned = account * rate
    total = account + interest_earned

    print("{0:<15} {1:<30.2f} {2:<25.2f} {3:.2f}".format(i, account, interest_earned, total))