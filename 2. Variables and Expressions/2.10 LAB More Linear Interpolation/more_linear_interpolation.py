#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 2.10 LAB: More Linear Interpolation
# Date: 3 9 2022

time_inital = 12 # in seconds
time_final = 85 # in seconds
xyz_o = (8, 6, 7) # in meters
xyz = (-5, 30, 9) # in meters

def linear_interpolation(distance_inital: int, distance_final: int, time: int) -> int:
    slope = (distance_final - distance_inital) / (time_final - time_inital)
    distance = slope * (time - time_inital) + distance_inital

    return distance

times = [30.0, 37.5, 45.0, 52.5, 60.0] # in seconds

for e, t in enumerate(times):
    print(f'At time {t} seconds:')
    print(f'x{e+1} = {linear_interpolation(xyz_o[0], xyz[0], t)} m')
    print(f'y{e+1} = {linear_interpolation(xyz_o[1], xyz[1], t)} m')
    print(f'z{e+1} = {linear_interpolation(xyz_o[2], xyz[2], t)} m')
    if t != times[-1]: print('-----------------------')

