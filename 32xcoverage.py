#!/usr/bin/env python3

# Write a program that simulates random read coverage over a chromosome
# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line
# Note that you will not sample the ends of a chromosome very well
# So don't count the first and last parts of a chromsome

import sys
import random

genome = int(sys.argv[1])
number = int(sys.argv[2])
read = int(sys.argv[3])
count = [0]*genome
for i in range(number): 
    init = random.randint(0,genome-read)
    for j in range (init, init+read):
        count[j] += 1
min=count[read+1]
max=count[read+1]
total=0
for i in range(read, genome-read): 
    if min >= count[i]: 
        min = count[i]
    if max <= count[i]: 
        max = count[i]
total = 0
for i in range(read, genome-read): 
    total += count[i]
average=total/(genome-2*read)
print(min, max, f'{average:.5f}')
#print(count)

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
