#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
# Section:      522
# Assignment:   3.16 LAB: Still More Linear Interpolation
# Date:         9 9 2022

# initial values
time_initial = float(input("Enter time 1: "))
x_initial = float(input("Enter the x position of the object at time 1: "))
y_initial = float(input("Enter the y position of the object at time 1: "))
z_initial = float(input("Enter the z position of the object at time 1: "))

# final values
time_final = float(input("Enter time 2: "))
x_final = float(input("Enter the x position of the object at time 2: "))
y_final = float(input("Enter the y position of the object at time 2: "))
z_final = float(input("Enter the z position of the object at time 2: "))

step = (time_final - time_initial) / 4
times = [time_initial + x * step for x in range(5)]


def linear_interpolation(distance_initial: int, distance_final: int, time: int) -> int:
    slope = (distance_final - distance_initial) / (time_final - time_initial)
    distance = slope * (time - time_initial) + distance_initial

    return distance


for t in times:
    x = linear_interpolation(x_initial, x_final, t)
    y = linear_interpolation(y_initial, y_final, t)
    z = linear_interpolation(z_initial, z_final, t)
    print(f"At time {t:.2f} seconds the object is at ({x:.3f}, {y:.3f}, {z:.3f})")
