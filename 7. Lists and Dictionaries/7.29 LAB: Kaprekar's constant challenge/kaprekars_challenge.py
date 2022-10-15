#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 7.29 LAB: Kaprekar's constant challenge
# Date: 10 14 2022

def kaprekar(number):
    # Take any four-digit number that has at least two
    # different digits (add leading zeros to numbers
    # with fewer than four digits)

    if len(set(str(number))) == 1 and len(str(number)) == 4:
        return 1

    if number == "6174":
        return 1

    count = 0
    while number != "6174":
        # Sort the digits in descending and then in ascending
        # order to get two four-digit numbers, adding
        # leading zeros if necessary
        descending = int(''.join(sorted(str(number), reverse=True)))
        ascending = int(''.join(sorted(str(number))))

        # Subtract the smaller number from the bigger number
        # to get a new four-digit number
        number = max(descending, ascending) - min(descending, ascending)
        number = str(number).zfill(4)

        count += 1

    return count

# some tests
assert kaprekar("3524") == 3
assert kaprekar("2111") == 5
assert kaprekar("9831") == 7
assert kaprekar("6174") == 1
assert kaprekar("1111") == 1
assert kaprekar("0007") == 4
assert kaprekar("0000") == 1
assert kaprekar("0025") == 7
assert kaprekar("0137") == 5
assert kaprekar("2026") == 6
assert kaprekar("3524") == 3
assert kaprekar("5432") == 3
assert kaprekar("7777") == 1
assert kaprekar("9998") == 5

total = sum(kaprekar(f"{i:04}") for i in range(10000))
print(f"Kaprekar's routine takes {total} total iterations for all four-digit numbers")
