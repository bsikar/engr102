# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   12.15 LAB: Matplotlib example
# Date:         11 18 2022
# As a team, we have gone through all required sections of the
# tutorial, and each team member understands the material

import matplotlib.pyplot as plt
import numpy as np

# plot two parabola as lines on the same plot
# the domain is x = [-2, 2] for f = 2 and f = 6
# y = 1/(4f) * x^2
x = np.linspace(-2, 2, 100)

plt.plot(x, 1 / (4 * 2) * x ** 2, label="f = 2", color="r")
plt.plot(x, 1 / (4 * 6) * x ** 2, label="f = 6", color="b")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Parabola plots with varying focal length")
plt.legend()
plt.show()

# plot (x, y) points for the cubic polunomial
# y = 2x**3 + 3x**2 - 11x - 6
# the domain is [-4, 4]
# 25 points in the domain are plotted
x = np.linspace(-4, 4, 25)
y = 2 * x ** 3 + 3 * x ** 2 - 11 * x - 6

# plot yellow filled in stars as the points
plt.plot(x, y, "y*", label="Cubic Polynomial", markeredgecolor="k")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Cubic Polynomial")
plt.legend()
plt.show()

# plot the sine and cosine functions on the same plot
# but on different axes
# the domain is x = [-2pi, 2pi]

x = np.linspace(-2 * np.pi, 2 * np.pi, 100)

plt.subplot(2, 1, 1)
plt.title("Plot of cos(x) and sin(x)")
plt.ylabel("y = cos(x")
plt.plot(x, np.cos(x), label="cos(x)", color="r")
plt.grid(True)
plt.xticks(
    np.linspace(-2 * np.pi, 2 * np.pi, 7),
    [],
)
# have only 3 y ticks
plt.yticks(np.linspace(-1, 1, 3))
plt.legend()
plt.subplot(2, 1, 2)
plt.plot(x, np.sin(x), label="sin(x)", color="b")
plt.ylabel("y = sin(x)")
plt.xlabel("x")
plt.legend()
plt.grid(True)
plt.yticks(np.linspace(-1, 1, 3))
plt.show()
