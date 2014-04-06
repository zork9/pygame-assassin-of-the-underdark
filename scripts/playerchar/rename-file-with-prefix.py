#!/usr/bin/env python

from os import rename,listdir
import sys
if len(sys.argv) <= 2: 
	print "Usage : rename-file-with-prefix.py [badprefix] [replacement-prefix]"
	sys.exit(0)
 
badprefix = sys.argv[1]
goodprefix = sys.argv[2]

fnames = listdir('.')

for fname in fnames:
	if fname.startswith(str(badprefix)):
		rename(fname, goodprefix + fname[len(badprefix):])


