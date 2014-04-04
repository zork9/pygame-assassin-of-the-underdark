#!/usr/bin/python

######### ./outputplayer elf fighter Elf Fighter

# Copyright (C) Johan Ceuppens 2014
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from filelines2list import *
from gplheader2list import *
import sys

# command line args in a list
args = str(sys.argv)

if len(sys.argv) < 5 or len(sys.argv) > 5:
	print "Usage : outputplayer.py [playerrace] [playerclass] [Capitalplayerrace] [Capitalplayerclass]\n"	
	sys.exit

race = sys.argv[1]
klass = sys.argv[2]
Race = sys.argv[3]
Klass = sys.argv[4]


def outputplayerracefile():
	f = open("./player" + race + ".py", "w")    ### .close() # touch file
	if f == None:
		print "Error : opening file\n"
		sys.exit

	for line in gplheader2list():
		f.write(line)

	f.write("\n")

	f.write("import pygame\n")
	f.write("from pygame.locals import *\n")
	f.write("\n")
	f.write("class Player" + Race + ":\n")
	f.write("\t\"Player " + Race + "\"\n")
	f.write("\tdef __init__(self):\n")
	f.write("\t\t1\n")
	# f.write("\n")
     	

outputplayerracefile() 
