#!/usr/bin/env python3
# 61dust.py

import argparse
import mcb185
import math

# Write a program that finds and masks low entropy sequence
# Use argparse for the following parameters
#   sequence file
#   window size
#   entropy threshold
#   lowercase or N-based masking
# The program should output a FASTA file (but with Ns or lowercase)
# Use argparse
# Use the mcb185.read_fasta() function
# Put more functions in your mcb185.py library

parser = argparse.ArgumentParser(description='Detect Sequence with Low Entropy')

parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='input the file name')
parser.add_argument('--window', required=False, type=int, default=11,
	metavar='<int>', help='Reading window size [%(default)i]')
parser.add_argument('--threshold', required=False, type=float, default=1.5,
	metavar='<float>', help='Reading window size [%(default).3f]')
parser.add_argument('--N', action='store_true',
	help='Switch for "N"')

arg = parser.parse_args()
'''
print(arg.fasta, arg.window, arg.threshold)
'''
def entropy(DNA): 
    dict = {}
    for nt in DNA:
        if nt not in dict:
            dict[nt]=0
        dict[nt] += 1
    sum = 0
    for key, val in dict.items(): 
        log = math.log((val/len(DNA)), 2)
        sum += -(val/len(DNA))*log
    return sum

window = arg.window
threshold = arg.threshold

for name, seq in mcb185.read_fasta(arg.fasta):
    seq=seq.upper()
    out = ""
    for i in range(len(seq) - window +1): 
        fragment = seq[i:i+window]
        judge = entropy(fragment)
        if judge <= threshold: 
            if arg.N: 
                out += "N"
            else: 
                out += seq[i].lower()
        else: 
            out += seq[i]
    for i in range(len(seq) - window +1, len(seq)): 
        out += seq[i]
    print(f">{name}")
    for i in range(0, len(out), 60): 
        print(out[i:i+60])

