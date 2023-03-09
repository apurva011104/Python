#Program to find the area and circumference of a circle when the radius is entered by the user.

import math
r=float(input("enter the value of radius: "))
print("Area: {0} sq.units \nCircumference: {1} units".format((math.pi)*r*r,2*(math.pi)*r))
