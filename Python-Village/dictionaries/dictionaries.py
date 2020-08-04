##!/usr/bin/env python3


f_in = open('rosalind_ini6.txt')
string = f_in.read()
words = string.split()


freq = {}

# loops through all words and updates count in freq{}
# if not in freq{},  word is added as a key and the value is set at 0 then incremented
for i in words:
    if i not in freq:
        freq[i] = 0
    freq[i] += 1

for key, value in freq.items():
    print(key, value)




