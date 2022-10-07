#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 2.11 LAB: Python Code Soup
# Date: 9 9 2022

# can only use:
# x = 1
# y = 10
# z = 0
# x = y
# x += 1
# y += x
# y *= x
# z += x
# z += y
# print(z)
#
# produces:
# 1
# 26
# 102
# 1000000000
# 8675

x = 1
z = 0
z += x
print(z)  # x = 1, z = 1 y = Err

y = 10
x += 1
y += x
y *= x
y += x
z = 0
z += y
print(z)  # x = 2, z = 26, y = 26

y = 10
x = y
y *= x
x = 1
x += 1
y += x
z = 0
z += y
print(z)  # x = 2, z = 102, y = 102

y = 10
x = y
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
y *= x
z = 0
z += y
print(z)  # x = 10 z = 1000000000 y = 1000000000

z = 0
y = 10
y *= x
x = 1
x += 1
x += 1
x += 1
x += 1
z += x
x += 1
y *= x
x += 1
z += y  # x = 7, y = 600, z = 605
y = 10
y *= x
z += y  # x = 7, y = 70, z = 675
x += 1
y = 10
y *= x
x += 1
x += 1
y *= x
y *= x
z += y
print(z)
