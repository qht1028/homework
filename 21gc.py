#!/usr/bin/env python3

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
# Use all three formatting methods

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT' # feel free to change
count=0
for i in range(0,len(dna),1): 
    if dna[i]=='G' or dna[i]=='C': 
        count+=1 
GC=count/len(dna)
print(f'{GC:.2f}')
print('{:.2f}'.format(GC))
print('%.2f' % (GC))


"""
python3 21gc.py
0.42
0.42
0.42
"""
