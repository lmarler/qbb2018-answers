#!/usr/bin/env python3

#/Users/cmdb/qbb2018-answers/day1-afternoon/SRR072893/SRR072983.sam

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin

count = 0
for line in f:
    if line.startswith( "SRR" ):
        count += 1
print(count)

f.seek(0)
Total = 0
for line in f:
    if line.startswith( "SRR" ):
        cut_line = line.strip().split("\t")
        Total += int(cut_line[4])
print(Total)

avg_mapq = Total / count
print(avg_mapq)