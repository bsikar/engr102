#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment:  7.28 LAB: Kaprekar's constant
# Date: 10 14 2022

number = int(input("Enter a four-digit integer: "))

nums = [number]

if len(set(str(number))) == 1 and len(str(number)) == 4:
    print(f"{number} > 0\n{number} reaches 0 via Kaprekar's routine in 1 iterations")
    exit()

while number != 6174:
    num = str(number)
    while len(num) < 4:
        num = "0" + num
    num = sorted(num)
    num1 = int("".join(num))
    num2 = int("".join(num[::-1]))
    number = num2 - num1
    nums.append(number)

# print the list with > between each number
print(" > ".join(str(x) for x in nums))
print(f"{nums[0]} reaches 6174 via Kaprekar's routine in {len(nums)-1} iterations")
