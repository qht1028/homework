#!/usr/bin/env python3

import gzip
import sys
import argparse
import re
import itertools
import mcb185

parser = argparse.ArgumentParser(description='Alternative Splicing Product Prediction')

parser.add_argument('--fasta', required=True, type=str,
	metavar='<str>', help='input the file name')
parser.add_argument('--exon', required=False, type=int, default=35,
	metavar='<int>', help='input the threshold for exon length [%(default)i]')
parser.add_argument('--intron', required=False, type=int, default=35,
	metavar='<int>', help='input the threshold for intron length [%(default)i]')

arg = parser.parse_args()

 

def potentialsite(seq): 
    #donor site check and list building
    donorlist = []
    for match in re.finditer("GT", seq):
        donorlist.append(int(match.start()))
    #acceptor site check and list building
    acceptorlist = []
    for match in re.finditer("AG", seq):
        acceptorlist.append(int(match.end()))
    return donorlist, acceptorlist

def illegaltransc(donors, acceptors):
    #check for too short intron
    for d, a in zip(donors, acceptors): 
        if d > a - arg.intron: 
            return True
    # check for too short exon 
    for i in range(len(donors) - 1): 
        a = acceptors[i]
        d = donors[i+1] 
        if d < a + 35: 
            return True 

splicecount = 0
for name, seq in mcb185.read_fasta(arg.fasta):
    donorlist, acceptorlist = potentialsite(seq)
    for i in range(len(donorlist)): 
        # key to give the all possible splicing consequence, regardless of accuracy
        for donorsites in itertools.combinations(donorlist, i + 1):
            for acceptorsites in itertools. combinations(acceptorlist, i + 1 ): 
                if illegaltransc(donorsites, acceptorsites): 
                    continue
                #count the number of isoform
                splicecount += 1
                print(f'transcript {splicecount}')
                print(f'donor sites {donorsites}; acceptor sites {acceptorsites}')
                #according to feasible splicing position, give the splicing product 
                transcript = ""
                for j in range(len(donorsites)): 
                    if transcript == "": 
                        transcript += seq[0:donorsites[0]]
                    else: 
                        transcript += seq[acceptorsites[j-1]:donorsites[j]]
                transcript += seq[acceptorsites[-1]:len(seq)+1]
                print(transcript)
    
'''    
for i in range(len(donorlist)): 
    for donorsites in itertools.combinations(donorlist, i + 1):
        for acceptorsites in itertools. combinations(acceptorlist, i + 1 ): 
            if illegaltransc(donorsites, acceptorsites): 
                continue
            print(donorsites, acceptorsites)
'''            
