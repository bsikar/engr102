#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jacob Gonzalez
#               Robert Moreno Garcia
#               Jinyu Zhou
# Section:      522
# Assignment:   2.8 LAB: Linear Interpolation
# Date:         1 9 2022

import math

time_inital = 10 # in minutes
time_final = time_inital + 45 # in minutes
distance_inital = 2026 # in kilometers
distance_final = 23_026 # in kilometers
iss_orbit_radius = 6_745 # in kilometers

"""
Instructions

Write a program that determines, for any time between 10 and 55 minutes, where the ISS will be (in
terms of kilometers past Houston). The time to evaluate at should be a variable in your program. The
program should print both the time and the position at that time to the screen, with a line describing
what is being output (see example output below). You should test your program at various times and
make sure the results seem reasonable.

---

Goal

For your final program that you submit, output the position at a time of 25 minutes. (Next week, we
will see how you can read in numbers from a user, but for now, just assume it is a fixed number of
minutes.)
"""

# Part 1

def linear_interpolation(time: int) -> int:
    # the x-axis is time
    # the y-axis is position

    slope = (distance_final - distance_inital) / (time_final - time_inital)
    distance = slope * (time - time_inital) + distance_inital
    distance %= 2 * math.pi * iss_orbit_radius

    return distance

time = 25 # in minutes
print("Part 1:")
print(f"For t = {time} minutes, the position p = {linear_interpolation(time)} kilometers")

time = 300 # in minutes
print("Part 2:")
print(f"For t = {time} minutes, the position p = {linear_interpolation(time)} kilometers")

