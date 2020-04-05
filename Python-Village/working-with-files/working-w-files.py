##!/usr/bin/env python3

f_out = open('output.txt', 'w+')
f_in = open('rosalind_ini5.txt', 'r')

i = 1
for line in f_in.readlines():
    if i % 2 == 0:
        f_out.write(str(line))
    i += 1


f_out.close()
