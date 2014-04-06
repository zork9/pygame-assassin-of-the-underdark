
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

# example:    self.northwall1 = Tilebox(1,1,60,48,16,1,'./pics/walldungeon1-60x48.bmp')
#               draws 16 times the picture from left to right 1 high

import pygame
from pygame.locals import *
from time import *
from gameobject import *

class Exit:
    "box"
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
 
    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	 player.x < self.x+room.relativex + self.w and 
	 player.y > self.y+room.relativey and 
	 player.y < self.y+room.relativey + self.h):
	    print "collision in Exit"	
	    return 1 
	else:
	    return 0

    def collidewithenemy(self, room, enemy):
	if (enemy.x > self.x  and 
	enemy.x < self.x+self.w*self.nx and 
	enemy.y - enemy.h > self.y and 
	enemy.y - enemy.h < self.y + self.h*self.ny):
	    #print "collision in Exit with enemy!"	
	    return 1 
	else:
	    return 0

