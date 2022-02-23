#!/usr/bin/env python3

import sys

# Write a program that predicts if a protein is trans-membrane
# Trans-membrane proteins have the following properties
#	Signal peptide: https://en.wikipedia.org/wiki/Signal_peptide
#	Hydrophobic regions(s): https://en.wikipedia.org/wiki/Transmembrane_protein
#	No prolines in hydrophobic regions (alpha helix)
# Hydrophobicity is measued via Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot
# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa
# Hints:
#   Create a function for KD calculation
#   Create a function for amphipathic alpha-helix

polypeptides = []
name = ""
seq = ""
with open(sys.argv[1]) as fp: 
    for line in fp.readlines():
        line=line.rstrip()
        if len(line)==0:
            continue
        if line[0] == ">":
            if name != "": 
                polypeptides.append((name, seq))
            words = line[1:].split()
            name = words[0] 
            seq = ""
        else: 
            seq += line
    polypeptides.append((name, seq))

def transmembrane(name, protein): 
    frame1 = 8
    frame2 = 11
    keypoint = 30
    signal = 0
    helix = 0
    for i in range(keypoint + 1 - frame1): 
        kd = 0
        for j in range(i, i+8): 
            if   protein[j] == 'I': kd += 4.5
            elif protein[j] == 'V': kd += 4.2
            elif protein[j] == 'L': kd += 3.8
            elif protein[j] == 'F': kd += 2.8
            elif protein[j] == 'C': kd += 2.5
            elif protein[j] == 'M': kd += 1.9
            elif protein[j] == 'A': kd += 1.8
            elif protein[j] == 'G': kd += -0.4
            elif protein[j] == 'T': kd += -0.7
            elif protein[j] == 'S': kd += -0.8
            elif protein[j] == 'W': kd += -0.9
            elif protein[j] == 'Y': kd += -1.3
            elif protein[j] == 'P': kd += -1.6
            elif protein[j] == 'H': kd += -3.2
            elif protein[j] == 'E': kd += -3.5
            elif protein[j] == 'Q': kd += -3.5
            elif protein[j] == 'D': kd += -3.5
            elif protein[j] == 'N': kd += -3.5
            elif protein[j] == 'K': kd += -3.9
            elif protein[j] == 'R': kd += -4.5
        if kd >= 2.5: 
            signal += 1 
    judge = 0
    for i in range(keypoint, len(protein) + 1 - frame2):
        kd = 0
        for j in range(i, i+8): 
            if   protein[j] == 'I': kd += 4.5
            elif protein[j] == 'V': kd += 4.2
            elif protein[j] == 'L': kd += 3.8
            elif protein[j] == 'F': kd += 2.8
            elif protein[j] == 'C': kd += 2.5
            elif protein[j] == 'M': kd += 1.9
            elif protein[j] == 'A': kd += 1.8
            elif protein[j] == 'G': kd += -0.4
            elif protein[j] == 'T': kd += -0.7
            elif protein[j] == 'S': kd += -0.8
            elif protein[j] == 'W': kd += -0.9
            elif protein[j] == 'Y': kd += -1.3
            elif protein[j] == 'P': kd += -1.6
            elif protein[j] == 'H': kd += -3.2
            elif protein[j] == 'E': kd += -3.5
            elif protein[j] == 'Q': kd += -3.5
            elif protein[j] == 'D': kd += -3.5
            elif protein[j] == 'N': kd += -3.5
            elif protein[j] == 'K': kd += -3.9
            elif protein[j] == 'R': kd += -4.5
        if kd >= 2.0: 
            helix += 1
    return(name, signal, helix)

for name, protein in polypeptides: 
    name, signal, helix = transmembrane(name, protein)
    if signal > 1 and helix > 1: 
        print(name)
"""
python3 40transmembrane.py ../Data/at_prots.fa
AT1G75120.1
AT1G10950.1
AT1G75110.1
AT1G74790.1
AT1G12660.1
AT1G75130.1
"""
