
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
from stateimagelibrary import *
import random
from time import *
from math import *

class Snake1(Gameobject):
    "Snake"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 88
        self.h = 48
        self.PI = 3.14182829
        self.hitpoints = 3
        
		
        self.headimage = pygame.image.load('./pics/snakehead1-48x48.bmp').convert()
        self.headimage.set_colorkey((0,0,0)) 
		
        self.bodyimage = pygame.image.load('./pics/snakebody1-48x48.bmp').convert()
        self.bodyimage.set_colorkey((0,0,0)) 
	
	self.talkcounter = 0
	self.direction = "down"

        self.angle = sqrt(2)/2

    def draw(self, screen, room):
        sleep(.1) # FIX goblin sleep
        self.angle += self.PI/8
        self.x -= 10
        self.y = sin(self.angle)*20
        screen.blit(self.bodyimage, (self.x+room.relativex,self.y+room.relativey))
        self.angle += self.PI/8
        self.y = sin(self.angle)*20
        screen.blit(self.bodyimage, (self.x-10+room.relativex,self.y+room.relativey))
        self.angle += self.PI/8
        self.y = sin(self.angle)*20
        screen.blit(self.bodyimage, (self.x-20+room.relativex,self.y+room.relativey))
        self.angle += self.PI/8
        self.y = sin(self.angle)*20
        screen.blit(self.bodyimage, (self.x-30+room.relativex,self.y+room.relativey))

        self.angle += self.PI/8
        self.x -= 10
        self.y = sin(self.angle)*20
        screen.blit(self.headimage, (self.x-40+room.relativex,self.y+room.relativey))
        self.angle -= self.PI/8
        self.angle -= self.PI/8
        self.angle -= self.PI/8
	     
    def update(self,room,player):
        1

    def collide(self, room, player):
        
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Snake!"
	    return 2 
	else:
	    return 0 ## for game self.talker

    def fight(self,room,player):
        1
