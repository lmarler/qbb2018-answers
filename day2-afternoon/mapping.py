#!/usr/bin/env python3

#Usage: 
#./mapping/py <file1> <file2> 
#./mapping/py <UniProtIDs> <ctab file>
#option -d as third argument prints "No match." for IDs not find in ctab file.

#Command line input 1 (sys.argv[1]) = .txt file containing FlyIDs and UniProtIDs
#Command line input 2 (sys.argv[2]) = ctab file
#Command line input 3 (sys.argv[3]) = "-d" or nothing

import sys

if len(sys.argv) > 2:
    f1=open(sys.argv[1])
    f2=open(sys.argv[2])
else:
    f=sys.stdin

dict = {}

for line in f1:
    fields1 = line.rstrip("\r\n").split()
    dict[fields1[0]] = fields1[1]
    
for line in f2:
    fields2 = line.rstrip("\r\n").split("\t")
    if line.startswith("t_id"):
        continue
    else:
        fields2 = line.rstrip("\r\n").split()
        ctab_flyID = fields2[8]
    
    if ctab_flyID in dict.keys():
        UniproID = dict[ctab_flyID]
        print (line + "\t" + UniproID)
    else:
        if len(sys.argv) > 3:
            if (sys.argv[3])=="-d":
                print ("No match.")



  
                
