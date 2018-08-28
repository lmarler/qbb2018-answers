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
        if cut_line[2]=="2L" and int(cut_line[3])>=10000 and int(cut_line[3])<=20000:
            count += 1
print(count)