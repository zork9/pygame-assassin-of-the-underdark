
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
from rng import *
from time import *

class Snake2(Gameobject):
    "Snake static left and right pic"
    def __init__(self,xx,yy):
	Gameobject.__init__(self, xx, yy)
        self.w = 36
        self.h = 36

        self.hitpoints = 2
        
	self.stimlibleft = Stateimagelibrary()	
	self.stimlibright = Stateimagelibrary()	
	self.stimlibdown = Stateimagelibrary()	
	self.stimlibup = Stateimagelibrary()	
        image = pygame.image.load('./pics/snakeleft1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)	
        image = pygame.image.load('./pics/snakeleft1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibleft.addpicture(image)
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)	
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibright.addpicture(image)
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibdown.addpicture(image)	
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibdown.addpicture(image)
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibup.addpicture(image)	
        image = pygame.image.load('./pics/snake1-48x48.bmp').convert()
        image.set_colorkey((0,0,255)) 
	self.stimlibup.addpicture(image)

	self.talkcounter = 0
	self.direction = "left"

    def draw(self, screen, room):
	if (self.direction == "left"):
            self.stimlibleft.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "right"):
            self.stimlibright.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "down"):
            self.stimlibdown.draw(screen, self.x+room.relativex,self.y+room.relativey)
	elif (self.direction == "up"):
            self.stimlibup.draw(screen, self.x+room.relativex,self.y+room.relativey)
	    
	     
    def update(self,game):
        ###sleep(.04) # FIX goblin sleep
	if game.room.collidewithenemy(self):
	    if (self.direction == "right"):
	        self.x -=4
	        self.direction = "left" 
	    elif (self.direction == "left"):
	        self.x +=4
	        self.direction = "right"
	    elif (self.direction == "down"):
	        self.y -=4
	        self.direction = "up" 
	    elif (self.direction == "up"):
	        self.y +=4
	        self.direction = "down"

	if game.player.x+28-game.room.relativex < self.x:
		self.x -= 2
		self.direction = "left"
	if game.player.x-28-game.room.relativex > self.x:
		self.direction = "right"
		self.x += 2	
	if game.player.y+10-game.room.relativey < self.y:
		self.direction = "up"
		self.y -= 2
	if game.player.y-10-game.room.relativey > self.y:
		self.direction = "down"
		self.y += 2

    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h +self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0 ## for game self.talker


    def fight(self,room,player):
        self.fightcounter = 1
        o = player.collidewithenemyweapon(room,self)
        if o:
            player.hitwithenemyweapon(RNG().rollsnakebite())
