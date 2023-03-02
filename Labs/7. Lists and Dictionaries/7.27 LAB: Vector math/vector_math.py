#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 7.27 LAB: Vector math
# Date: 10 14 2022

def add_vectors(a, b):
    return map(sum, zip(a, b))

def sub_vectors(a, b):
    # we can use the add_vectors function to subtract vectors
    return add_vectors(a, [-i for i in b])

def dot_product(a, b):
    return sum([i * j for (i, j) in zip(a, b)])

def magnitude(a):
    return (sum([i ** 2 for i in a])) ** 0.5

a = [float(x) for x in input("Enter the elements for vector A: ").split()]
b = [float(x) for x in input("Enter the elements for vector B: ").split()]

print(f"The magnitude of vector A is {magnitude(a):.5f}")
print(f"The magnitude of vector B is {magnitude(b):.5f}")
print(f"A + B is {list(add_vectors(a, b))}")
print(f"A - B is {list(sub_vectors(a, b))}")
print(f"The dot product is {dot_product(a, b):.2f}")
