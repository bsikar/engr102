#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   8.10 LAB: ASCII clock
# Date:         10 19 2022

# dictionary of numbers
numbers = {
    "0": ["000", "0 0", "0 0", "0 0", "000"],
    "1": [" 1 ", "11 ", " 1 ", " 1 ", "111"],
    "2": ["222", "  2", "222", "2  ", "222"],
    "3": ["333", "  3", "333", "  3", "333"],
    "4": ["4 4", "4 4", "444", "  4", "  4"],
    "5": ["555", "5  ", "555", "  5", "555"],
    "6": ["666", "6  ", "666", "6 6", "666"],
    "7": ["777", "  7", "  7", "  7", "  7"],
    "8": ["888", "8 8", "888", "8 8", "888"],
    "9": ["999", "9 9", "999", "  9", "999"],
    ":": [" ", ":", " ", ":", " "],
}

# user input
time = input("Enter the time: ")

# empty new line
print()

""" print the time """
# loop for the length of each list
# in the numbers dictionary
for i in range(5):
    # loop for the length of the time
    for j in range(len(time)):
        # look up the number in the dictionary
        # and print the number
        print(numbers[time[j]][i], end=" ")
    # print the new line
    print()
