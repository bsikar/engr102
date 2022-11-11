#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 11.11 LAB: Barcode checker
# Date: 11 11 2022

file = input("Enter the name of the file: ")
output_file = open("valid_barcodes.txt", "w")
valid_count = 0
with open(file, "r") as f:
    barcodes = f.read().splitlines()
    for barcode in barcodes:
        if len(barcode) != 13:
            continue
        first_half = sum(map(int, barcode[:12:2]))
        second_half = sum(map(int, barcode[1:13:2])) * 3
        last_digit = str(first_half + second_half)[-1]
        if 10 - int(last_digit) == int(barcode[-1]):
            # write to file
            output_file.write(barcode + "\n")
            valid_count += 1
# close file
output_file.close()

print(f"There are {valid_count} valid barcodes")
