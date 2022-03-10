import mcb185 as mcb
import sys
import itertools
from itertools import permutations
from itertools import combinations 

filename = sys.argv[1]
frame = 100
for name, seq in mcb.read_fasta(filename):
    for k in range(1, frame): 
        print(k)
        kmerdict = {}
        for i in range(len(seq)-k+1): 
            kmer = seq[i:i + k] 
            kmerdict[kmer] = True
        if len(kmerdict.keys()) < 4**k: 
            limit = k
            print(len(kmerdict.keys()))
            break

count = 0
for ktup in itertools.product("ATGC", repeat=limit): 
        kmer = ''.join(ktup)
        if kmer not in kmerdict: 
            print(kmer)
            count += 1
print(count)
