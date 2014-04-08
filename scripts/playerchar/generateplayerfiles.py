#!/usr/bin/python

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
###############################################
# Note that the syntax is Magicuser based, Thief and Fighter
#
# ./generateplayerfiles.py elf fightermagicuser Elf FighterMagicuser ELF FIGHTERMAGICUSER
#
# ./generateplayerfiles.py elf "fighter magicuser" Elf "Fighter Magicuser" ELF FIGHTERMAGICUSER
#
# ./generateplayerfiles.py elf fighter Elf Fighter ELF FIGHTER
#
###############################################

# command line args in a list
args = str(sys.argv)

if len(sys.argv) < 7 or len(sys.argv) > 7:
	print "Usage : outputplayer.py [playerrace] [playerclass] [Capitalplayerrace] [Capitalplayerclass] [RACE] [CLASS]\n"	
	sys.exit(0)

race = sys.argv[1]
klass = sys.argv[2]
Race = sys.argv[3]
Klass = sys.argv[4]
RACE = sys.argv[5]
KLASS = sys.argv[6]


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
	f.write("\n")
     	
def outputplayerraceresourcesfile():
	f = open("./player" + race + "resources.py", "w")    ### .close() # touch file
	if f == None:
		print "Error : opening file\n"
		sys.exit

	for line in gplheader2list():
		f.write(line)

	f.write("\n")

	f.write("import pygame\n")
	f.write("from pygame.locals import *\n")
	f.write("from stateimageresourcelibrary import *\n")
	f.write("from imageresource import *\n")
	f.write("\n")
	f.write("class Player" + Race + "Resources" + ":\n")
	f.write("\t\"Player " + Race + " Resources" + "\"\n")
    	f.write("\tdef __init__(self):\n" +
        "\t\tself.stimlib = Stateimageresourcelibrary()\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter1-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter2-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter3-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter2-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter1-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter2-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighter3-48x48.bmp')\n" +
        "\t\tself.stimlib.addpicture(imageres)\n" +

        "\t\tself.stimlibfight = Stateimageresourcelibrary()\n"+
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight1-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight1-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight2-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight2-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight3-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
        "\t\timageres = ImageResource().load0('./pics/player" + race + klass + "fighterfight3-48x48.bmp')\n" +
        "\t\tself.stimlibfight.addpicture(imageres)\n" +
	"\n" +
    "\tdef askpicture(self):\n" +
        "\t\treturn './pics/taskbar-PC-fighter.bmp'\n")
	
	f.write("\n")

def outputplayerraceclassfile():
	f = open("./player" + race + klass + ".py", "w")    ### .close() # touch file
	if f == None:
		print "Error : opening file\n"
		sys.exit

	for line in gplheader2list():
		f.write(line)

	f.write("\n")

	f.write("import pygame\n")
	f.write("from pygame.locals import *\n")
	f.write("from playerbase import *\n")
	f.write("from player" + race + "resources" + " import *\n")
	f.write("\n")
	f.write("class Player" + Race + Klass + "(PlayerBase, Player" + Race + "Resources):\n")
	f.write("\t\"Player " + Race + " " + Klass + "\"\n")
	f.write("\tdef __init__(self):\n")
	f.write("\t\tPlayerBase.__init__(self,PlayerBase." + RACE + ", PlayerBase." + KLASS + ")\n")
	f.write("\t\tPlayer" + Race + "Resources.__init__(self)\n")
	f.write("\n")
	f.write("\tdef askclass(self):\n")
	f.write("\t\treturn " + "\"" + Klass + "\"\n") #### FIXME Magic User won't work
	f.write("\n")
	f.write("\tdef askrace(self):\n")
	f.write("\t\treturn " + "\"" + Race + "\"\n")
	f.write("\n")
     	
outputplayerracefile() 
outputplayerraceresourcesfile() 
outputplayerraceclassfile() 
