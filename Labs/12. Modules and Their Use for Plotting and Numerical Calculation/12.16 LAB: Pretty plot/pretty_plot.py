#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 12.16 LAB: Pretty plot
# Date: 11 18 2022

import matplotlib.pyplot as plt
import numpy as np

point = (0, 1)
matrix = np.array([1.01, 0.09, -0.09, 1.01]).reshape(2, 2)

# create a list with 200 points by multiplying the matrix by the point
# and adding the result to the list
points = [point]
for i in range(200):
    point = matrix.dot(point)
    points.append(point)

# plot the points
plt.plot([p[0] for p in points], [p[1] for p in points], "o")
plt.title(
    "An Archimedean like spiral from a 2x2 matrix multiplied by a point 200 times"
)
plt.xlabel("x")
plt.ylabel("y")
plt.legend(["points"])
plt.show()
