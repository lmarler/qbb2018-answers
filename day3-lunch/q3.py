#!/usr/bin/env python3

#Finds number of protein coding genes

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin
    
count = 0
find_pos = 21378950
current_dist = 10000000000
    
for line in f:
    if "!" in line:
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        if fields[2]=="gene" and fields[0]=="3R":
            my_dist = 0
            if find_pos < int(fields[3]):
                my_dist = int(fields[3]) - find_pos
            elif find_pos > int(fields[4]):
                my_dist = find_pos - int(fields[4])
      
            if my_dist < current_dist:
                current_dist = my_dist
                fields2 = fields[8].split()
                if (fields2[9])=="\"protein_coding\";": 
                    nearest_so_far = {}
                    nearest_so_far[(fields2[1])] = my_dist
                else:
                    nearest_so_far1 = {}
                    nearest_so_far1[(fields2[1])] = my_dist
                    
print ("Nearest protein coding gene", nearest_so_far)
print ("Nearest non-protein coding gene", nearest_so_far1)
                    
#print ("Nearest protein coding gene", fields2[1], my_dist)    
             
