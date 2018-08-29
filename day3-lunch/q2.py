#!/usr/bin/env python3

#Makes a dictionary with gene_biotype as key and number for each type as value.

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin
    
biotypes={}
    
for line in f:
    if "!" in line:
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        if fields[2]=="gene":
            fields2 = fields[8].split()       
            if fields2[9] in biotypes:
                biotypes[fields2[9]] += 1
            else:
                biotypes[fields2[9]] = 1
            
print (biotypes)


# counter = 0
# for x in y:
#     if something:
#         counter += 1
        
my_dict = {}
data = ['A', 'B', 'B', 'C', 'C','C']
for biotype in data:
    if biotype in my_dict:
        my_dict[biotype] += 1
    else:
        my_dict[biotype] = 1