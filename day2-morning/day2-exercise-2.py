#!/usr/bin/env python3

#/Users/cmdb/qbb2018-answers/day1-afternoon/SRR072893/SRR072983.sam

import sys

if len(sys.argv) > 1:
    f=open(sys.argv[1])
else:
    f=sys.stdin

count = 0
for line in f:
    if "NM:i:0" in line:
        count += 1
print(count)