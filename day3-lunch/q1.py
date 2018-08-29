#!/usr/bin/env python3

#Finds number of protein coding genes

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin
    
count = 0
    
for line in f:
    if "!" in line:
        continue
    else:
        fields = line.rstrip("\r\n").split("\t")
        if fields[2]=="gene":
            fields2 = fields[8].split()
            if (fields2[9])=="\"protein_coding\";": 
                count += 1
print (count)
#            s = "gene_biotype*"
#            s2 = "protein_coding"
#            print (s.find(s2))


            
#            def find_str(s, char):
#                index = 0
#            
#                if char in s:
#                        c = char[0]
#                        for ch in s:
#                            if ch == c:
#                                if s[index:index+len(char)] == char:
#                                    return index
#
#                            index += 1
#                gene_biotypes = []
#                gene_biotypes.append(find_str("protein_coding"))
                
                
#            fields2 = fields[8].split("; ")
#            print (fields2[7])
 
#print (count)
    
    
#pull out genes that have fields[2]=="gene"
#pull out string from these lines that starts.with("gene_biotype") and is 29 characters long
#take strings that contain "protein_coding"