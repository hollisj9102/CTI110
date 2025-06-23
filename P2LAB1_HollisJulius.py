# Juilis Hollis
# 06-23-2025
# P2LAB1 – Circle Measurements
# This program asks the user for the radius of a circle and calculates the
# diameter, circumference, and area. It then displays the results with 
# specific decimal formatting.

import math

# Ask the user to input the radius of a circle
radius = float(input("Enter the radius of the circle: "))

# Calculate diameter, circumference, and area
diameter = 2 * radius
circumference = 2 * math.pi * radius
area = math.pi * radius ** 2

# Display the results with specified formatting
print("Diameter      : {:.1f}".format(diameter))
print("Circumference : {:.2f}".format(circumference))
print("Area          : {:.3f}".format(area))
