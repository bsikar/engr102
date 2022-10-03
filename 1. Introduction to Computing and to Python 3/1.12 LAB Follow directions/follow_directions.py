#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 1.12 LAB: Follow directions
# Date: 26 8 2022


"""
instructions

Write a program named follow_directions.py that performs the following tasks for the function f(x) = (x^2 − 1)/(x − 1) evaluated close to x = 1. Use values of x ranging from 1.1 to 1.00000001 by inserting another zero after the decimal of the previous value (x = 1.1, x = 1.01, x = 1.001…).

1. First, print a line of text stating the purpose of the program
2. Next, print a line of text stating your guess for the final calculated value
    - There are no wrong answers, just make a guess
    - Think about the answer then see if your guess was close
3. Next, print out a sequence of 8 numbers, representing evaluating the function at 8 different values of x
4. Finally, print one blank line, followed by a statement of how good your guess is


This shows the evaluation of tan(x)/x evaluated close to x=0
My guess is 2
1.5574077246549023
1.0033467208545055
1.0000333346667207
1.0000003333334668
1.0000000033333334
1.0000000000333333
1.0000000000003333
1.0000000000000033

My guess was a little off
"""

print("This shows the evaluation of (x^2-1)/(x-1) evaluated close to x=1")
print("My guess is 2")

# try looping to print
x = 1.1
print((x ** 2 - 1) / (x - 1))
for _ in range(7):
    x = float(str(x).replace(".", ".0"))
    print((x ** 2 - 1) / (x - 1))

print("\nMy guess was alright")
