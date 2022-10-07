#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 3.17 LAB: Using input
# Date: 12 9 2022

# import math
import math

print("This program calculates the applied force given mass and acceleration")
mass = float(input("Please enter the mass (kg): "))
acceleration = float(input("Please enter the acceleration (m/s^2): "))
force = mass * acceleration
print(f"Force is {force:.1f} N")


print("This program calculates the wavelength given distance and angle")
distance = float(input("Please enter the distance (nm): "))
angle = float(input("Please enter the angle (degrees): "))
wavelength = 2 * distance * math.sin(math.radians(angle))
print(f"Wavelength is {wavelength:.4f} nm")


print(
    "This program calculates how much Radon-222 is left given time and initial amount"
)
days_left = float(input("Please enter the time (days): "))
inital_amount = float(input("Please enter the initial amount (g): "))
half_life = 3.8  # in days
radon_222 = inital_amount * 2 ** (-days_left / half_life)
print(f"Radon-222 left is {radon_222:.2f} g")


print("This program calculates the pressure given moles, volume, and temperature")
moles = float(input("Please enter the number of moles: "))
volume = float(input("Please enter the volume (m^3): "))
temperature = float(input("Please enter the temperature (K): "))
gas_constant = 8.314  # in J mol^-1 K^−1
pressure = (moles * gas_constant * temperature) / volume / 1000
print(f"Pressure is {pressure:.0f} kPa")
