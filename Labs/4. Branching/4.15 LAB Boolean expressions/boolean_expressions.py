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
# Assignment:   4.15 LAB: Boolean expressions
# Date:         9 19 2022

############ Part A ############
num_true = 0


def to_bool(x):
    global num_true
    if x in ["False", "F", "f"]:
        return False
    if x in ["True", "T", "t"]:
        num_true += 1
        return True


a = to_bool(input("Enter True or False for a: "))
b = to_bool(input("Enter True or False for b: "))
c = to_bool(input("Enter True or False for c: "))

############ Part B ############
print(f"a and b and c: {a and b and c}")
print(f"a or b or c: {a or b or c}")

############ Part C ############
def nand(x, y):
    return not (x and y)


def xor(x, y):
    return (not (x and y)) and (not (not x and not y))


print(f"XOR: {xor(a, b)}")
print(f"Odd number: {num_true == 1 or num_true == 3}")

############ Part D ############
complex1 = (
    (not (a and not b) or (not c and b))
    and (not b)
    or (not a and b and not c)
    or (a and not b)
)
complex2 = (
    (not ((b or not c) and (not a or not c)))
    or (not (c or not (b and c)))
    or (a and not c)
    and (not a or (a and b and c) or (a and ((b and not c) or (not b))))
)
simple1 = (not a and not c) or not b
simple2 = a or (not b and c)

print(f"Complex 1: {complex1}")
print(f"Complex 2: {complex2}")
print(f"Simple 1: {simple1}")
print(f"Simple 1: {simple2}")
