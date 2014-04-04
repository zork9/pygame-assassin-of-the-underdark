
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
from sword import *
from fireballspell import *
from goblin1 import *
from goblin2 import *
from goblin3 import *
from tilebox import *
from snake1 import *
from snake2 import *
from rubysword import *
from beholder import *
from beholderbat import *
from centipede import *
from gnome import *
from butterflydemon import *

class Maproom1(MaproomDungeon):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomDungeon.__init__(self,x,y)
        self.background = pygame.image.load('./pics/room-bg1.bmp').convert()
        self.northwall1 = Tilebox(1,1,60,48,13,1,'./pics/walldungeonnorth1-60x48.bmp')
        self.southwall1 = Tilebox(1,200,30,48,13,1,'./pics/walldungeonsouth1-30x48.bmp')
        self.westwall1 = Tilebox(360,200,48,60,1,10,'./pics/walldungeonwest1-48x60.bmp')
        self.eastwall1 = Tilebox(775,1,48,60,1,14,'./pics/walldungeoneast1-48x60.bmp')
        self.tileboxes.append(self.northwall1)
        self.tileboxes.append(self.westwall1)
        self.tileboxes.append(self.eastwall1)
        self.tileboxes.append(self.southwall1)

        self.gameobjects.append(Sword(100,120))
        self.gameobjects.append(FireballSpell(500,120))

        self.gameobjects.append(Goblin3(300,100))
        self.gameobjects.append(Goblin3(340,140))
        self.gameobjects.append(Goblin3(380,180))
        self.gameobjects.append(Goblin3(400,100))
        self.gameobjects.append(Goblin3(440,120))

        self.gameobjects.append(Goblin3(440,520))
        self.gameobjects.append(Goblin3(480,520))
        self.gameobjects.append(Goblin3(520,520))
        self.gameobjects.append(Goblin3(560,520))
        self.gameobjects.append(ButterflyDemon(500,500))

        self.gameobjects.append(Goblin3(540,620))
        self.gameobjects.append(Goblin3(580,620))
        self.gameobjects.append(Goblin3(620,620))
        self.gameobjects.append(Goblin3(660,620))

    def isroomdownexit(self,game):
	if self.relativex  < -250 and self.relativex > -650 and self.relativey < -650:
		return 1
	return 0

    def setxyfromdown(self,game):
        game.setxy(0,0)

    def exit(self, game):
	if self.isroomdownexit(game):
		self.setxyfromdown(game)
		return 2
	return 0 
 
