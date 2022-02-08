#!/usr/bin/env python3

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# E.g. python3 entropy.py 0.4 0.3 0.2 0.1
# Put the probabilities into a new list
# Don't forget to convert them to numbers

import math
import sys

sum=0
total=0
val=[]
for i in range(1,len(sys.argv)): 
    val.append(float(sys.argv[i]))

for i in range(len(val)): 
    sum += val[i]
if abs(1-sum) > 0.01:
    print(sum)
    print("failure")
else: 
    for i in range(len(val)):
        log = math.log(val[i], 2)
        total += -val[i]*log
    print(f'{total:.3f}')


"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
