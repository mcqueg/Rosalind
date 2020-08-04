##!/usr/bin/env python3

# Given: A DNA string s of length at most 1000 nt
# Return: four integers separated by spaces representing the count for 'A', 'C', 'G', 'T'

# Sample Dataset:  AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC
# Sample Output: 20 12 17 21


f_in = open('rosalind_dna.txt')
dna = f_in.read()

a_count = 0
c_count = 0
g_count = 0
t_count = 0

for i in dna:
    if i == 'A':
        a_count += 1
    elif i == 'C':
        c_count += 1
    elif i == 'G':
        g_count += 1
    elif i == 'T':
        t_count += 1
    else:
        break

print(a_count, c_count, g_count, t_count)
