#!/usr/bin/env python


# Create a greeter
#    create a greeter that says hello to someone in all lower case.  Use print statements
#
#  ex:
#   >>> greeter("paul")
#   hello, paul
#   >>> greeter(3)
#   hello, 3
#   >>> greeter("WORLD")
#   hello, world

# def greeter(name):

def greeter(name):
    name = str(name)
    print "hello,", name.lower() #Prints "hello," then the name converted into lower-case.


# Draw a box
#    given a width and a height, draw a box in the terminal.  Use print statements
#
#  ex:
#    >>> box("apples", -3)
#    Error: Invalid Dimensions
#    >>> box(1,1)
#    +
#    >>> box(4,2)
#    +--+
#    +--+
#    >>> box(3,3)
#    +-+
#    | |
#    +-+

# def box(w,h):

def box(width, height):

# Checking if the users inputs are compatible dimensions for the box.
    if width <= 0 or height <= 0 or type(width)!=int or type(height)!=int:
        print "Error: Invalid Dimensions"
        return

# Printing the first "+" and "|" for the box.
    corner1 = "+"
    edge1 = "|"

#If the width is greater than or equal to 2 (meaning it would have 2 "+"s and "|"s)
    if width >= 2:
        corner2 = "+"
        edge2 = "|"

    else:
        corner2 = ""
        edge2 = ""

    topgate = "-" * (width - 2)
    rowspace = " " * (width - 2)
    top = corner1 + topgate + corner2 #Sets the variable for the code for the top of the box.
    row = edge1 + rowspace + edge2 #Sets the variable for the row for the box.
    
    print top #Prints the top of the box (needs to be printed for the top and the bottom) so twice.
    for i in range(height - 2):
        print row #Prints the row.
    if height > 1:
        print top #Prints the bottom of the box (same as the top).

##!!!! We never really went over functions in class, this was really difficult.


