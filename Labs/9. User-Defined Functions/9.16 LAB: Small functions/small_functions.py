#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 9.16 LAB: Small functions
# Date: 10 28 2022

from math import pi

# Imagine that you have a spherical bead. In other words, a sphere
# with a cylindrical hole drilled through the middle:
# Write a function named parta that will take in as parameters the radius of
# the sphere and the radius of the hole, and return the volume of the bead.
# input: 1, 0.25 -> output: 3.802293
# input: 1, 0.5 -> output: 2.720699
# input: 1, 0.95 -> output: 0.127525
def parta(sphere_radius, hole_radius):
    # Thank GOD for https://mathhelpforum.com/threads/finding-the-volume-of-a-bead.63161/post-231194
    # I was having the hardest time with this question
    R = sphere_radius
    r = hole_radius
    return ((4 * pi) / 3) * (R ** 2 - r ** 2) ** (3 / 2)

# Write a function named partb that will take in as a parameter a positive integer n and
# determines if n can be calculated as the sum of 2 or more consecutive positive, odd integers.
# If it can, return a list of the numbers, otherwise return False.
# 15 -> [3, 5, 7]
# 75 -> [11, 13, 15, 17, 19] or [23, 25, 27]
def partb(n):
    n = int(n)
    # Loop through the numbers from 1 to n
    for i in range(1, n, 2):
        # Create a list of consecutive odd numbers
        numbers = [i]
        # Loop through the numbers from 1 to n
        for j in range(i + 2, n, 2):
            # Add the number to the list
            numbers.append(j)
            # If the sum of the numbers in the list is equal to n, return the list
            if sum(numbers) == n:
                return numbers
    # If no list of consecutive odd numbers add to n, return False
    return False


# Write a function named partc that will take in as parameters a single character, a person’s
# name, company, and email, and returns a single string of the person’s digital business card. Use
# the character as a border, and provide 2 spaces as padding on either side of the longest entry.
# example:
# Example using parameters
# partc('*', 'Dr. Ritchey', 'Texas A&M University', 'snritchey@tamu.edu'):
# **************************
# *      Dr. Ritchey       *
# *  Texas A&M University  *
# *   snritchey@tamu.edu   *
# **************************
def partc(border_character, name, company, email):
    # Find the length of the longest string
    longest = max(len(name), len(company), len(email))
    # Add 2 to the length of the longest string to account for the padding
    longest += 2
    # Create a string that is the border with the length of the longest string
    border = border_character * (longest + 4)
    # Create a string that is the name with the length of the longest string
    name = name.center(longest)
    # Create a string that is the company with the length of the longest string
    company = company.center(longest)
    # Create a string that is the email with the length of the longest string
    email = email.center(longest)
    # Return the border, name, company, email, and border
    return f"""{border}
{border_character} {name} {border_character}
{border_character} {company} {border_character}
{border_character} {email} {border_character}
{border}"""


# Write a function named partd that takes in as a parameter one list of numbers and returns the
# minimum, median, and maximum value of the list, in that order.
def partd(numbers):
    # Sort the list of numbers
    numbers.sort()
    # Find the length of the list of numbers
    length = len(numbers)
    # If the length of the list of numbers is odd, then the median is the middle number
    if length % 2 == 1:
        median = numbers[length // 2]
    # If the length of the list of numbers is even, then the median is the average of the two middle numbers
    elif length % 2 == 0:
        median = (numbers[length // 2] + numbers[length // 2 - 1]) / 2
    # Return the minimum, median, and maximum value of the list
    return numbers[0], median, numbers[-1]


# Write a function named parte that takes in as parameters two parallel lists: a list of times (in
# increasing order), and a list of distances traveled by that point in time. The function should
# return a new list giving the velocity between consecutive time measurements. The new list
# should have a length of one less than the original lists.
def parte(times, distances):
    # Create a new list
    velocities = []
    # Loop through the list of times
    for i in range(len(times) - 1):
        # Calculate the velocity between the two times
        velocity = (distances[i + 1] - distances[i]) / (times[i + 1] - times[i])
        # Add the velocity to the new list
        velocities.append(velocity)
    # Return the new list
    return velocities


# Write a function named partf that takes in as a parameter one list of numbers and determines if
# two of the numbers in the list add to 2026. If they do, return the product of the two numbers,
# otherwise return False.
def partf(numbers):
    # Loop through the list of numbers
    for i in range(len(numbers)):
        # Loop through the list of numbers again
        for j in range(len(numbers)):
            # If the two numbers add to 2026, return the product of the two numbers
            if numbers[i] + numbers[j] == 2026:
                return numbers[i] * numbers[j]
    # If no two numbers add to 2026, return False
    return False


if __name__ == "__main__":
    functions = [parta, partb, partc, partd, parte, partf]
    for function in functions:
        while True:
            user_input = input(
                f"Enter the parameters for {function.__name__} separated by commas: "
            )
            if user_input == "exit":
                exit()
            elif user_input == "next":
                break
            try:
                # if its a number convert it to a number
                user_input = [
                    float(i) if i.replace(".", "", 1).isdigit() else i
                    for i in user_input.split(",")
                ]
                print(function(*user_input))
            except Exception as e:
                print(e)
