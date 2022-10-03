#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
# Section:      522
# Assignment:   3.15 LAB: Unit Conversions
# Date:         9 9 2022

# get input from user
quantity = float(input("Please enter the quantity to be converted: "))

# define functions
def pounds_to_newtons(pounds):
    return pounds * 4.4482216153

def meters_to_feet(meters):
    return meters * 3.28084

def atmospheres_to_kilopascals(atmospheres):
    return atmospheres * 101.325

def watts_to_btu(watts):
    return watts * 3.412141633

def liters_to_gallons(liters):
    return liters * 15.850323141489

def celsius_to_fahrenheit(celsius):
    return celsius * (9 / 5) + 32

# print statements
print(f"{quantity:.2f} pounds force is equivalent to {pounds_to_newtons(quantity):.2f} Newtons")
print(f"{quantity:.2f} meters is equivalent to {meters_to_feet(quantity):.2f} feet")
print(f"{quantity:.2f} atmospheres is equivalent to {atmospheres_to_kilopascals(quantity):.2f} kilopascals")
print(f"{quantity:.2f} watts is equivalent to {watts_to_btu(quantity):.2f} BTU per hour")
print(f"{quantity:.2f} liters per second is equivalent to {liters_to_gallons(quantity):.2f} US gallons per minute")
print(f"{quantity:.2f} degrees Celsius is equivalent to {celsius_to_fahrenheit(quantity):.2f} degrees Fahrenheit")
