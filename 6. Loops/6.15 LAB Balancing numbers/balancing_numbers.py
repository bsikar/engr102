#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 6.15 LAB: Balancing numbers
# Date: 10 6 2022

user_n = int(input("Enter a value for n: "))
# cannot use sum() because cringe
total = 0
for i in range(1, user_n):
    total += i

# get the numbers after user_n that add up to total
loop_total = 0
for r, i in enumerate(range(user_n + 1, total + 1)):
    loop_total += i
    if loop_total == total:
        print(f"{user_n} is a balancing number with r={r+1}")
        exit()
    elif loop_total > total:
        break
print(f"{user_n} is not a balancing number")
