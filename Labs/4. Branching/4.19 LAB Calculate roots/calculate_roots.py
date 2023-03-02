#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Brighton Sikarskie
# Section:      522
# Assignment:   4.19 LAB: Calculate roots
# Date:         9 20 2022

import math

a = float(input("Please enter the coefficient A: "))
b = float(input("Please enter the coefficient B: "))
c = float(input("Please enter the coefficient C: "))

discriminant = b**2 - 4 * a * c
if a == 0:
    # if a and b are both 0 then c has to be 0
    # if just a then root = -c / b
    if b == c == 0:
        print("The root is x = 0")
    elif b != 0:
        root = -c / b
        print(f"The root is x = {root}")
    else:
        print("You entered an invalid combination of coefficients!")
elif discriminant > 0:
    # if the discriminant is greater than 0 then the roots
    # are real and are different
    roots = sorted(
        [
            (-b + math.sqrt(discriminant)) / (2 * a),
            (-b - math.sqrt(discriminant)) / (2 * a),
        ],
        reverse=True,
    )
    print(f"The roots are x = {roots[0]} and x = {roots[1]}")
elif discriminant < 0:
    # if the discriminant is less than 0 then there
    # are 1 real and 1 imaginary roots
    real = -b / (2 * a)
    imaginary = math.sqrt(-discriminant) / (2 * a)
    print(f"The roots are x = {real} + {imaginary}i and x = {real} - {imaginary}i")
else:
    # if the discriminant is 0 then the roots
    # are equal
    root = -b / (2 * a)
    print(f"The root is x = {root}")
