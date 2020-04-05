##!/usr/bin/env python3

f_out = open('output.txt', 'w+')
odd_sum = 0

with open('rosalind_ini4.txt', 'r') as input:
    data = input.read().split(' ')
range(int(data[0]), int(data[1]))
for i in range(int(data[0]), int(data[1])+1):
    if (i % 2 == 0):
        continue
    else:
        odd_sum = odd_sum + i

output = f_out.write(str(odd_sum))
print(odd_sum)
