#!/usr/bin/env python3

#/Users/cmdb/qbb2018-answers/day1-afternoon/SRR072893/SRR072983.sam

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin
    
count = 0
for line in f:
    if line.startswith("SRR"):
        cut_line = line.strip().split("\t")
        print (cut_line[2])
        count += 1
        if count > 9:
            break