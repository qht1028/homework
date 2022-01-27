#!/usr/bin/env python3

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

dna = 'ACTGAAAAAAAAAAA'
antidna=""
for i in range (len(dna)-1, -1, -1):
    if dna[i] == 'A': antidna += "T"
    elif dna[i] == 'T': antidna += "A"
    elif dna[i] == 'G': antidna += "C"
    else: antidna += "G"
print(antidna)
    
"""
python3 23anti.py
TTTTTTTTTTTCAGT
"""
