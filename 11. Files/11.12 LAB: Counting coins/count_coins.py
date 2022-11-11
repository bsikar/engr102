#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 11.12 LAB: Counting coins
# Date: 11 11 2022

output = open("coins.txt", "w")
with open("game.txt") as f:
    coins = f.read().splitlines()
    total = 0
    i = 0
    while i < len(coins):
        mv, num = coins[i].split()
        if mv == "coin":
            total += int(num)
            # write to file
            output.write(f"{int(num)}\n")
        elif mv == "jump":
            i += int(num)
            continue
        i += 1
output.close()

print(f"Total coins collected: {total}")
