
# Copyright (C) Johan Ceuppens 2010-2014
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

class ButterflyDemon(Gameobject):
    ""
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 66 
        self.h = 50
	self.stimlib = Stateimagelibrary()
        image = pygame.image.load('./pics/butterflydemon1-66x50.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)	
        image = pygame.image.load('./pics/butterflydemon2-66x50.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/butterflydemon3-66x50.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)
	image = pygame.image.load('./pics/butterflydemon4-66x50.bmp').convert()
        image.set_colorkey((255,255,255)) 
	self.stimlib.addpicture(image)

	self.direction = "left"

    def draw(self, screen, room):
        self.stimlib.draw(screen, self.x+room.relativex,self.y+room.relativey)    
	     
    def update(self,room,player):
        sleep(.005)
##        self.x-=1
	if (random.randint(0,14) == 0 and self.direction == "left"):
	   self.direction = "right"
        if (random.randint(0,13) == 0 and self.direction == "right"):
	   self.direction = "left"
        if (random.randint(0,12) == 0 and self.direction == "down"):
	   self.direction = "up"
	if (random.randint(0,10) == 0 and self.direction == "up"):
	   self.direction = "down"

	if (not self.collideobjectX(room)): 
	    if (self.direction == "left"):
	        self.x +=2
	        self.direction = "right" 
	    elif (self.direction == "right"):
	        self.x -=2
	        self.direction = "left"

	if (not self.collideobjectY(room)): 
	    if (self.direction == "up"):
	        self.x +=2
	        self.direction = "down" 
	    elif (self.direction == "down"):
	        self.x -=2
	        self.direction = "up"


	if (self.direction == "left"):
	        self.x -=1 
	elif (self.direction == "right"):
	        self.x +=1
	elif (self.direction == "down"):
	        self.y +=1
	elif (self.direction == "up"):
	        self.y -=1
	        

    def collide(self, room, player):
	if (player.x > self.x+room.relativex  and 
	player.x < self.x+room.relativex+self.w and 
	player.y > self.y+room.relativey and 
	player.y < self.y+room.relativey + self.h):
	    print "collision with Butterflydemon!"
	return 0

		 
