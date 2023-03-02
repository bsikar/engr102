#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   4.13.1 LAB: Make change
# Date:         9 9 2022
quarter, dime, nickel, penny = 25, 10, 5, 1
num_quarter, num_dime, num_nickel, num_penny = 0, 0, 0, 0

# user input
pay = float(input("How much did you pay? "))
cost = float(input("How much did it cost? "))
change = round((pay - cost) * 100)

# printing change amount
print(f"You received ${(pay - cost):.2f} in change. That is...")

num_quarter = change // quarter
amount = quarter * num_quarter
if amount > 0:
    change -= amount

num_dime = change // dime
amount = dime * num_dime
if amount > 0:
    change -= amount

num_nickel = change // nickel
amount = nickel * num_nickel
if amount > 0:
    change -= amount

num_penny = change // penny
amount = penny * num_penny
if amount > 0:
    change -= amount

# checking if we should print the 's'
if num_quarter > 1:
    print(int(num_quarter), "quarters")
elif num_quarter > 0:
    print("1 quarter")
if num_dime > 1:
    print(int(num_dime), "dimes")
elif num_dime > 0:
    print("1 dime")
if num_nickel > 1:
    print(int(num_nickel), "nickels")
elif num_nickel > 0:
    print("1 nickel")
if num_penny > 1:
    print(int(num_penny), "pennies")
elif num_penny > 0:
    print("1 penny")
