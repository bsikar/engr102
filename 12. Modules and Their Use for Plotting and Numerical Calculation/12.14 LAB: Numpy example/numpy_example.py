# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   12.14 LAB: Numpy example
# Date:         11 14 2022
# PART A #
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material
import numpy as np

# PART B #
A = np.arange(12).reshape(3, 4)
B = np.arange(8).reshape(4, 2)
C = np.arange(6).reshape(2, 3)
print(f"A = {A} \n")
print(f"B = {B} \n")
print(f"C = {C} \n")
# PART C #
D = np.dot(np.dot(A, B), C)
print(f"D = {D} \n")
# PART D #
print(f"D^T = {np.transpose(D)} \n")
# PART E #
E = np.sqrt(D) / 2
print(f"E = {E}")
