#!/usr/bin/env python3

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median
# No, you cannot import the stats library!

import sys
import math

val=[]
for i in range(1,len(sys.argv)): 
    val.append(float(sys.argv[i]))
    
min=val[0]
max=val[0]
sum=0
sd=0
  
for i in range(len(val)):
    sum += val[i]
    if min >= val[i]: 
        min = val[i]
    if max <= val[i]:
        max = val[i]
mean=sum/len(val)
for i in range(len(val)):
    sd += (mean-val[i])**2
sd=(sd/len(val))**0.5

val.sort()
if len(val) % 2 == 1:
    median = val[int(len(val)/2)]
else: 
    median = (val[int(i/2)]+val[int((i+2)/2)])/2

print("Count: ", len(sys.argv))
print("Minumum: " f'{float(min):.3f}')
print("Maximum: " f'{float(max):.3f}')
print("Mean: " f'{float(mean):.3f}')
print("Std. dev: " f'{float(sd):.3f}')
print("Median: " f'{float(median):.3f}')


"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
