#!/usr/bin/env python3

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# No, you may not use math.factorial()
# Use the same loop for both calculations

n = 5

# your code goes here

a=0
b=0
c=1
for i in range (1,n+1,1): 
    a=a+1
    b=b+i
    c=c*i

print(a,b,c)

"""
python3 11sumfac.py
5 15 120
"""
