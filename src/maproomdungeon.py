
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
from koboldwizard import *
from time import *
from maproomdungeonnorthwall import *
from maproomdungeonsouthwall import *
from maproomdungeonwestwall import *
from maproomdungeoneastwall import *
from maproombase import *

class MaproomDungeon(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.northwalls = []
        self.southwalls = []
        self.westwalls = []
        self.eastwalls= []
        self.gameobjects = []
        self.tileboxes = []
        self.pits = []

    def removegameobject(self, o):
	for o2 in self.gameobjects:
		if o2 == o:
			self.gameobjects.remove(o)
       			return
 
    def addnorthwall(self, x,y):
        self.northwalls.append(MaproomNorthDungeonWall(x,y))

    def addsouthwall(self, x,y):
        self.southwalls.append(MaproomSouthDungeonWall(x,y))

    def addwestwall(self, x,y):
        self.westwalls.append(MaproomWestDungeonWall(x,y))

    def addeastwall(self, x,y):
        self.eastwalls.append(MaproomEastDungeonWall(x,y))
        
    def draw(self,game):
        # draw bg
        game.screen.blit(self.background, (self.relativex, self.relativey))
        for w in self.northwalls:
            w.draw(game.screen,self.relativex,self.relativey)
        # draw walls
        for t in self.tileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        # draw gameobjects
        for i in self.gameobjects:
	    if i != None:
		i.update(game)
		i.draw(game.screen,self)
      
    def collide(self, player):	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		return 2 # 1 kills game
	for i in self.northwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.southwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.westwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.eastwalls:
	    if i != None and i.collide(self, player):
		return 2
	for i in self.tileboxes:
		if i != None and i.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2 
	for i in self.pits:
		if i != None and i.collide(self,player):
			return 2
	return 0

    def collidewithenemy(self, enemy):
	for t in self.tileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
        return 0

    def collidebarehands(self,game):
        for i in self.gameobjects:
	    if i!= None:
		#self.relativex = self.prevx
		#self.relativey = self.prevy
	    	id = i.collidewithbarehands(self,game.player)
		if id:
			return i ## NOTE : returns collided entity (single)
	return None

    def collidesword(self,game):
        for i in self.gameobjects:
	    if i!= None:
		#self.relativex = self.prevx
		#self.relativey = self.prevy
	    	id = i.collidewithsword(self,game.player)
		if id:
			return i ## NOTE : returns collided entity (single)
	return None

    def hitwithsword(self, o, game):
        hitp = o.hit(game)
        if hitp < 0:
            self.removeobject(o)

    def hitwithbarehands(self, o, game):
        hitp = o.hit(game)
        if hitp < 0:
            self.removeobject(o)

    def removeobject(self, o):
        for i in range(0,len(self.gameobjects)):
            if self.gameobjects[i] == o:
                self.gameobjects[i] = None

