#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Brighton Sikarskie
# Section:      522
# Assignment:   4.18 LAB: How many gadgets
# Date:         9 20 2022

# Assume a machine during its initial testing phase produces 5 gadgets a day.
# On day 11, it begins to run at full speed, producing 50 gadgets per day.
# On day 61, it produces 1 fewer gadget per day
# On day 101 it stops producing gadgets.

# Rules: cannot use loops
# Soo.. use recursion :)

def get_gadgets(day: int) -> int:
    if day <= 10: return 5 * day
    if day <= 60: return 50 + get_gadgets(day - 1)
    if day <= 100: return 110 - day + get_gadgets(day - 1)
    return get_gadgets(day - 1)

day = int(input("Please enter a positive value for day: "))
if day < 0: print("You entered an invalid number!")
else: print(f"The total number of gadgets produced on day {day} is {get_gadgets(day)}")
