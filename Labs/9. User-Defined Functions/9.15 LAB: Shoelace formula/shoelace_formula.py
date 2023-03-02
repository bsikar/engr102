# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Brighton Sikarskie
#               Jason Garcia
#               David Paige
#               Erick Hernandez
# Section:      522
# Assignment:   Lab: Topic 9.15 (team)
# Date:         10 28 2022

#function to make a list of lists of points from a string
def getpoints(s):
    return [[int(x) for x in point.split(",")] for point in s.split(" ")]

#function that calculates the cross product from two given points
def cross(a, b):
  return a[0] * b[1] - a[1] * b[0]

#function that applies the shoelace formula to a list of points
def shoelace(points):
    cross_ = [cross(points[i], points[i+1]) for i in range(len(points)-1)]
    cross_.append(cross(points[-1], points[0]))
    return sum(cross_) / 2

#main function
def main():
    area = shoelace(getpoints(input('Please enter the vertices: ')))
    print(f"The area of the polygon is {area}")

if __name__ == '__main__': 
    main() 