
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
from snake1 import *
from rubysword import *
from beholder import *
from beholderbat import *
from snake2 import *

class Maproom3(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg3.bmp').convert()

    def isroomupexit(self,game):
	if self.relativey < -650:
		return 1
	return 0

    def setxyfromup(self,game):
        game.setxy(0,0) 

    def exit(self, game):
	if self.isroomupexit(game):
		self.setxyfromup(game)
		return 5 
	return 0 
 
