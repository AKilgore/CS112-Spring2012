#!/usr/bin/env python

from random import randint

input_number = int(raw_input())
list1 = []

#Changes the line to include a random number.
for _ in range(input_number):
    list1.append(randint(0,20))

print list1

s = 1
while s:
    s = 0

    for var in range(1,input_number):
        if list1[var-1] > list1[var]:
            input_number1 = list1[var-1]
            input_number2 = list1[var]
            list1[var-1] = input_number2
            list1[var] = input_number1
            s = 1

#Prints list a second time.
print list1
