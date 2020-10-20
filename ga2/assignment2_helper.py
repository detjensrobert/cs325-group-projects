#!/usr/bin/env python3
import sys

import assignment2

infile = sys.argv[1]
outfile = sys.argv[2]

print("------")
max_score = assignment2.vankin_max_score(infile, outfile)
print("------")

print(f"Max score: {max_score}")
