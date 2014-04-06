
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
from inventorygameobject import *
from gameobjectresources import *

class Gameobject(GameobjectResources):
    "Game object"
    def __init__(self, xx,yy):
	GameobjectResources.__init__(self)
	self.x = xx 
        self.y = yy
	# default width and height 
        self.w = 48
        self.h = 48
        self.SCREENH = 300
        self.SCREENW = 300
	self.inventoryitem = InventoryGameobject()
        ## dungeon statue as default picture
        ## self.image = pygame.image.load('./pics/dungeon-statue1-36x36.bmp').convert()
        self.image = pygame.image.load('./pics/nopicture.bmp').convert()
        self.image.set_colorkey((0,0,0)) 
        self.hitpoints = 1
        # NOTE : decrease 1 hitpoint with default sword
	self.name = "Gameobject"
        
    def draw(self, screen, room):
        screen.blit(self.image,(self.x+room.relativex,self.y+room.relativey))
	    
	     
    def collidewithsword(self, room, player):
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0

    def collidewithbarehands(self, room, player):
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x-self.w  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y-self.h and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0

    def collide(self, room, player):
        # FIX BUG
        #print 'gameobject x=%d y=%d player x=%d y=%d' % (self.x,self.y,player.x-room.relativex,player.y-room.relativey)
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y and 
	player.y-room.relativey < self.y + self.h):
	    #print "collision with Game Object!"
	    return 1 
	else:
	    return 0 ## for game self.talker

    def collidepickup(self, room, player):
        # FIX BUG
	if (player.x-room.relativex > self.x  and 
	player.x-room.relativex < self.x+self.w and 
	player.y-room.relativey > self.y+self.h and 
	player.y-room.relativey < self.y+ self.h):
	    #print "pickup collision!"	
	    return 3 
	else:
	    return 0 
    
    def collideobjectX(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.x > i.x  and 
		    self.x < i.x+i.w):
	            return 1 
	return 0

    def collideobjectY(self, room):
	for i in room.gameobjects:
	    if i != None:	
	        if (self.y > i.y  and 
		    self.y < i.y+i.h):
	            return 1 
	return 0
 
    def collideobjectXY(self, room):
	for i in room.gameobjects:
	    if i:		
	        if (self.x > i.x  and 
	 	    self.x < i.x+i.w and 
	            self.y > i.y and 
	            self.y < i.y+i.h):
	            return 1 
	return 0 
    
    def update(self,game):
	1

    def pickup(self, room):
        return 0

    def talkto(self, room):
        return 0

    def gettalktext(self, game):
        return "You cannot talk to this thing." 

    def hitwithspell(self,game):
	if game.taskbar and game.taskbar.spellitem:
		damage = game.taskbar.spellitem.roll(game)
		if damage > 0:
            		print 'gameobject is hit with %d damage (spell) !' % damage
        		self.hitpoints -= damage

    def hitwithweapon(self,game):
	if game.taskbar and game.taskbar.sworditem:
		damage = game.taskbar.sworditem.roll(game)
		if damage > 0:
            		print 'gameobject is hit with %d damage !' % damage
        		self.hitpoints -= damage

    def hit(self, game):
	self.hitwithweapon(game)

    def fight(self,room,player):
	1
    
    def undomove(self):
	1
