#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 3.18 LAB: Calling functions
# Date: 12 9 2022

import math

# required function
def printresult(shape, side, area):
    print(f"A {shape} with side {side:.2f} has area {area:.3f}")


side_length = float(input("Please enter the side length: "))
triangle = math.sqrt(3) / 4 * side_length ** 2
square = side_length ** 2
pentagon = 1 / 4 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * side_length ** 2
dodecagon = 3 * (2 + math.sqrt(3)) * side_length ** 2

printresult("triangle", side_length, triangle)
printresult("square", side_length, square)
printresult("pentagon", side_length, pentagon)
printresult("dodecagon", side_length, dodecagon)
