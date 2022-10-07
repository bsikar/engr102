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
# Assignment:   6.12 LAB: Pyramid Area (Part 2)
# Date:         10 3 2022
from math import sqrt

side = float(input("Enter the side length in meters: "))
layers = int(input("Enter the number of layers: "))

# calculate bird eye view area, area of triangle
triangle_area = (sqrt(3) / 4) * (side * layers) ** 2

# finding the sides area or view from sides
square_area = layers * ((side * side + side * side * layers) / 2)

# add all visible areas
total_area = square_area * 3 + triangle_area

# print statement
print(f"You need {total_area:.2f} m^2 of gold foil to cover the pyramid")
