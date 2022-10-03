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
# Assignment:   4.14 LAB: Pretty equation
# Date:         9 19 2022

A = input("Please enter the coefficient A: ")
B = input("Please enter the coefficient B: ")
C = input("Please enter the coefficient C: ")
# ax^2 + bx + c

if A == "0":
    A = ""
elif A == "-1":
    A = "- x^2"
elif A == "1":
    A = "x^2"
else:
    A += "x^2"

prefix = ""

if A != "":
    if int(B) > 0:
        prefix = " + "
    else:
        prefix = " - "

if B == "0":
    B = ""
elif B == "1" or B == "-1":
    B = prefix + "x"
else:
    B = f"{prefix}{abs(int(B))}x"

if int(C) > 0:
    prefix = " + "

if C == "0":
    C = ""
elif A == B == "":
    C = f" {C}"
else:
    C = f"{prefix}{abs(int(C))}"

print(f"The quadratic equation is {A}{B}{C} = 0")
