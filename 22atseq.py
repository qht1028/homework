#!/usr/bin/env python3

import random
#random.seed(1) # comment-out this line to change sequence each time

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence


length = 30
dna=""
count=0
for i in range (length):
    r = random.randint(0, 4)
    if r <= 2:
        r= random.randint(1, 2)
        if r == 1: dna += "A"
        else: dna += "T"
    else: 
        r= random.randint(1, 2)
        if r == 1: dna += "G"
        else: dna += "C"
for i in range (length):
    if dna[i] == "A" or dna[i] == "T":
        count += 1 
ratio=count/length
print(length, ratio, dna)        

print()

length = 30
dna = ""
count = 0
for i in range (length):
    r=random. random()
    if r <= 0.3: 
        dna += "A"
        count += 1
    elif r <= 0.6: 
        dna += "T"
        count += 1
    elif r <= 0.8: dna += "G"
    else: dna += "C"
ratio=count/length
print(length, ratio, dna) 
    

"""
python3 22atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
