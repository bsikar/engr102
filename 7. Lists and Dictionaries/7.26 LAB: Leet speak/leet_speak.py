#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 7.26 LAB: Leet speak
# Date: 10 14 2022

# This program will convert a string to leet speak
def leet(word):
    dictionary_upper = {'A': '4', 'E': '3', 'O': '0', 'S': '5', 'T': '7'}
    dictionary_lower = {'a': '4', 'e': '3', 'o': '0', 's': '5', 't': '7'}
    dictionary = {**dictionary_upper, **dictionary_lower}

    return ''.join([dictionary.get(letter, letter) for letter in word])

word = input("Enter some text: ")
print(f'In leet speak, "{word}" is:\n{leet(word)}')
