##!/usr/bin/env python3


#GIVEN: two positive integers a and b,
#a < 1000, b < 1000
#RETURN: integer corresponding to the square of the hypotenuse of the right
#triangle whose legs have lengths a and b
#
#a = 3
#b = 5
#34
import math
f_out = open('output.txt', 'w+')

with open('rosalind_ini2.txt', 'r') as input:
    data = input.read().split(' ')

a = int(data[0])
b = int(data[1])
c = a ** 2 + b ** 2
output = f_out.write(str(c))

print(c)
