#!/usr/bin/env python3
import sys

import assignment3

infile = sys.argv[1]
outfile = sys.argv[2] or "/dev/null"

min_moves = assignment3.vidrach_itky_leda(infile, outfile)
