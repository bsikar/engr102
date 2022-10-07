#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 6.14 LAB: Juggler sequence
# Date: 10 6 2022

# get the user's number
from math import floor, sqrt

user_n = int(input("Enter a positive integer: "))


def alter(n):
    if n % 2 == 0:
        return floor(sqrt(n))
    else:
        return floor(n ** (3 / 2))


print(f"The Juggler sequence starting at {user_n} is:")
# loop until n = 1
times = 0
while user_n != 1:
    print(user_n, end=", ")
    user_n = alter(user_n)
    times += 1
print(f"1\nIt took {times} iterations to reach 1")
