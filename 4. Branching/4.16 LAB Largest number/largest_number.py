#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Brighton Sikarskie
# Section:      522
# Assignment:   4.16 LAB: Largest number
# Date:         9 19 2022

input1 = float(input("Enter number 1: "))
input2 = float(input("Enter number 2: "))
input3 = float(input("Enter number 3: "))
#print(f"The largest number is {max(input1, max(input2, input3)):.1f}")
largest = input1
if input1 < input2 < input3:
    larget = input3
elif input1 < input3 < input2:
    largest = input2
print(f"The largest number is {largest:.1f}")
