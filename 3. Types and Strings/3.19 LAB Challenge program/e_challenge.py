#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 3.19 LAB: Challenge program
# Date: 12 9 2022

from math import e

precision = int(input("Please enter the number of digits of precision for e: "))
print(f"The value of e to {precision} digits is: {e:.{precision}f}")
