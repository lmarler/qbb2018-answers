#!/usr/bin/env python3

#Finds matching k-mers between a single query sequence and a database of targets.
#Usage: kmer_matcher.py <target.fa> <query.fa> <k>
#Returns: target_sequence_name  [target_start]  [query_start]  k-mer

import sys
#import the module we made in fasta.py
import fasta

if len(sys.argv) > 2:
    target=open(sys.argv[1])
    query=open(sys.argv[2])
else:
    target=sys.stdin

reader = fasta.FASTAReader(query)

kmers = {}

if len(sys.argv) > 3:
    k = int(sys.argv[3])
else:
    k = 11

for ident, sequence in reader:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer not in kmers:
            kmers[kmer] = [i]
        else:
            kmers[kmer].append(i)
 
#for key in kmers:          
#    print (key, kmers[key])

reader = fasta.FASTAReader(target)
    
for ident, sequence in reader:
    for i in range(0, len(sequence)-k):
        kmer = sequence[i:i+k]
        if kmer in kmers:
            for key in kmers:
                print (ident, [i], kmers[key], key)
        