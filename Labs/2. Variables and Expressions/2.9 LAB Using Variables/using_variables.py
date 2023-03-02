#!/usr/bin/env python3

# By submitting this assignment, I agree to the following:
# "Aggies do not lie, cheat, or steal, or tolerate those who does"
# "I have not given or received any unauthorized aid on this assignment"
#
# Name: Brighton Sikarskie
# Section: 522
# Assignment: 2.9.1: LAB: Using Variables
# Date: 26 8 2022


"""
Instructions:

Calculate the force in Newtons applied to an object with mass 3 kg and acceleration 5.5 m/s^2. According to Newton’s Second Law the net force applied to an object produces a proportional acceleration.
    -> F = MA

Calculate the wavelength of x-rays scattering from a crystal lattice with a distance between crystal layers of 0.025 nm, scattering angle of 25 degrees, and first order diffraction. Bragg’s Law describes the scattering of waves from a crystal using the equation nλ = 2d sin θ The standard unit of wavelength in the SI system is nanometers (nm).
    -> nλ = 2d sin θ

Calculate how much Radon-222 is left after 3 days of radioactive decay given an initial amount of 5 g and a half-life of 3.8 days. The equation for radioactive decay is N(t) = N02^(−t/t_half) where N0 is the intial amount (units of grams), t is the time (units of days), and t1/2 is the half-life (units of days).
    -> N(t) = N02^(−t/t_half)


Calculate the pressure of 5 moles of an ideal gas with a volume of 0.25 m^3, and temperature of 415 K. The Ideal Gas Law is the equation of state of a hypothetical ideal gas and is a good approximation of the behavior of gases under many conditions. Use a value of 8.314 m^3Pa/K·mol for the gas constant. The standard unit of pressure in the SI system is kilopascals (kPa).
    -> PV = nRT
"""

# import math
import math

mass = 3  # in kg
acceleration = 5.5  # in m/s^2
force = mass * acceleration

distance = 0.025  # in nm
angle = 25  # in degrees
wavelength = 2 * distance * math.sin(math.radians(angle))

days_left = 3  # in days
inital_amount = 5  # in g
half_life = 3.8  # in days
radon_222 = inital_amount * 2 ** (-days_left / half_life)

moles = 5
volume = 0.25  # in m^3
temperature = 415  # in K
gas_constant = 8.314  # in J mol^-1 K^−1
pressure = (moles * gas_constant * temperature) / volume / 1000

print(f"Force is {force} N")
print(f"Wavelength is {wavelength} nm")
print(f"Radon-222 left is {radon_222} g")
print(f"Pressure is {pressure} kPa")
