#!/usr/bin/env python3
import sys

import assignment3

if len(sys.argv) == 1 or len(sys.argv) > 3:
    print(f"Usage: {sys.argv[0]} infile (outfile, opt.) ")
    exit(1)

infile = sys.argv[1]
outfile = sys.argv[2] if len(sys.argv) >= 3 else "/dev/null"

min_moves = assignment3.vidrach_itky_leda(infile, outfile)

print(f"Min moves: {min_moves}")
