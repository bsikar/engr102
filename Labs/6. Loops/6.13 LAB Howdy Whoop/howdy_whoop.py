#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 6.13 LAB: Howdy Whoop
# Date: 10 6 2022

# get the user's numbers
user_n1 = int(input("Enter an integer: "))
user_n2 = int(input("Enter another integer: "))
# loop through 1 to 100
for i in range(1, 101):
    # check if divisible by both
    if i % user_n1 == 0 and i % user_n2 == 0:
        print("Howdy Whoop")
    # check if divisible by the first
    elif i % user_n1 == 0:
        print("Howdy")
    # check if divisible by the second
    elif i % user_n2 == 0:
        print("Whoop")
    # otherwise, just print the number
    else:
        print(i)
