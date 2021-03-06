#!/uqsr/bin/env python3
# 52digest.py

import re
import sys

# Write a program that performs an EcoRI digest on the SARS-COV2 genome
# The program should have 2 arguments
#    1. The genome file
#    2. The restriction pattern
# The output should be the sizes of the restriction fragments


seq = ""
DNA = False
with open(sys.argv[1]) as fp:
    for line in fp.readlines():
        line=line.rstrip()
        words = line.split()
        if len(line) == 0:
            continue
        if words[0] == "ORIGIN":
            DNA = True
        if DNA: 
            for frag in words[1:]:
                seq += frag 
 
target = sys.argv[2]
def digest(sequence): 
    position = []
    previous = 0
    for match in re.finditer(target, sequence):
        current = (match.start()+match.end())/2
        position.append(int(current-previous))
        previous = current
    position.append(len(sequence)-int(current))
    return position
    
position = digest(seq)
print(position)
    
    
"""
python3 52digest.py ../Data/sars-cov2.gb gaattc
1160
10573
5546
448
2550
2592
3569
2112
1069
"""
