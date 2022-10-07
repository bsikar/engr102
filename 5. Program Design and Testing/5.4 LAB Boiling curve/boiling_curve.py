#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 5.4 LAB: Boiling curve
# Date: 9 26 2022

# we only need log10 so no need to import everything with `*`
from math import log10

# the user will enter the excess temperature
excess_temperature = float(input("Enter the excess temperature: "))

# default points provided
points = [
    (1.3, 1000),
    (5, 7000),
    (30, 1.5 * 10**6),
    (120, 2.5 * 10**4),
    (1200, 1.5 * 10**6),
]

# this function will be used in the get_equation function
def get_slope(po, p1):
    return log10(p1[1] / po[1]) / log10(p1[0] / po[0])


# this function will actually return the y value on the line
# by using the x value provided from the user (excess_temperature)
def get_equation(x):
    xo = 0
    for i in range(len(points)):
        if x >= points[i][0]:
            xo = i
    # point 'e' should never be the i
    (xo, yo), point_right = points[xo], points[xo + 1]
    return yo * (x / xo) ** get_slope((xo, yo), point_right)


# we need to check the bounds of the user input
# if the user entered excess_temperature was out of the
# bounds of the graph then we cannot do anything with
# that input since it doesnt 'exist'
if excess_temperature < 1.3 or excess_temperature > 1200:
    print("Surface heat flux is not available")
else:
    print(
        f"The surface heat flux is approximately {get_equation(excess_temperature):.0f} W/m^2"
    )
