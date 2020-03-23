##!/usr/bin/env python

#Given: A string s of length at most 200 letters and four
#integers a, b, c and d.

#Return: The slice of this string from indices a through b
#and c through d (with space in between), inclusively. In other
#words, we should include elements s[b] and s[d] in our slice.
f_out = open('output.txt', 'w+')

with open('rosalind_ini3.txt', 'r') as input:
    data = input.read().split('.')
    string = data[0]
    nums = data[1].split(' ')

a = int(nums[0])
b = int(nums[1]) + 1
c = int(nums[2])
d = int(nums[3]) + 1

string_1 = string[a:b]
string_2 = string[c:d]

answer = str(string_1) + " " + str(string_2)
output = f_out.write(answer)
print(answer)
