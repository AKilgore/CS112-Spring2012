#!/usr/bin/env python

# Distance formula
#   calculate a function called "distance" to calculate the distance between two points.
#   http://www.purplemath.com/modules/distform.htm
#   ex: 
#      >>> distance((0,0), (3,4))
#      5

# def distance(a, b):
import math

#Defines distance as a function, which performs the distance formula and returns the answer promptly
def distance((x1, y1), (x2, y2)):
    distance = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    return distance

#The user inputs four numbers, serving as the respective coordinates.
x1 = int(raw_input("Enter the first number in your first coordinate: "))
y1 = int(raw_input("Enter the second number in your first coordinate: "))
x2 = int(raw_input("Enter the first number in your second coordinate: "))
y2 = int(raw_input("Enter the second number in your second coordinate: "))

print "The distance between your two points is ", distance((x1, y1), (x2,y2))

