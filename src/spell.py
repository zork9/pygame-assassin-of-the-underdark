
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
from gameobject import *
from bombexplosion import *
from inventoryspell import *

class Spell(Gameobject):
    ""
    def __init__(self, xx,yy):
        Gameobject.__init__(self,xx,yy)
        self.w = 36
        self.h = 36
	self.collisionw = 64-self.w 
	self.collisionh = 64-self.h 
        self.image = pygame.image.load('./pics/spell1-36x36.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
   	self.counter = 0 
	self.inventoryitem = InventorySpell()

    def update(self,game):
	1

    def collide(self, room, player):
        #print 'spell x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x - self.collisionw and 
	player.x-room.relativex < self.x + self.w + self.collisionw and 
	player.y-room.relativey > self.y - self.collisionh and 
	player.y-room.relativey < self.y + self.h + self.collisionh):
	    #print "collision with Spell"
	    return 1 
	else:
	    return 0 ## for game self.talker

    def cast(self,game):
        print 'You cast %s' % self

