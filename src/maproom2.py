
# Copyright (C) Johan Ceuppens 2010
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


import pygame
from pygame.locals import *
from tree import *
from tree2 import *
from dungeonentrance1 import *
from maproomdungeon import *
from maproomdungeonnorthwall import *
from goblin1 import *
from goblin2 import *
from goblin3 import *
from tilebox import *
from dungeoncave import *
from snake1 import *
from rubysword import *
from beholder import *
from beholderbat import *
from snake2 import *

class Maproom2(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg2.bmp').convert()
###        self.westwall1 = Tilebox(1,1,48,60,1,14,'./pics/walldungeonwest2-48x60.bmp')
###        self.eastwall1 = Tilebox(775,1,48,60,1,14,'./pics/walldungeoneast1-48x60.bmp')
###        self.tileboxes.append(self.westwall1)
###        self.tileboxes.append(self.eastwall1)
        self.wall1 = Tilebox(600,500,100,100,2,1,'./pics/walldungeon1-100x100.bmp')
        self.tileboxes.append(self.wall1)

	# FIXME add collision boxes around the following exit
        self.cave = DungeonCave(500,500,100,100,'./pics/walldungeoncave2-100x100.bmp')
	self.tileboxes.append(Tilebox(500,500,100,65,1,1))
	self.tileboxes.append(Tilebox(500,500,65,100,1,1))
        self.exits.append(self.cave)

        self.gameobjects.append(Goblin3(100,100))
        self.gameobjects.append(Goblin3(150,100))
        self.gameobjects.append(Beholder(400,100))
        self.gameobjects.append(BeholderBat(300,300))

    def isroomupexit(self,game):
	if self.relativey < -650:
		return 1
	return 0

    def setxyfromcave(self,game):
        game.setxy(0,0) 

    def isroomcaveexit(self,game):
	if self.cave.collide(self, game.player):
		return 1
	return 0

    def setxyfromup(self,game):
        game.setxy(0,0) 

    def exit(self, game):
	if self.isroomupexit(game):
		self.setxyfromup(game)
		return 4 
	if self.isroomcaveexit(game):
		self.setxyfromcave(game)
		return 3 
	return 0 
 
