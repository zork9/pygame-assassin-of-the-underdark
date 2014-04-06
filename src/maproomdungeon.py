
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
import math 
from maproomdungeonnorthwall import *
from maproomdungeonsouthwall import *
from maproomdungeonwestwall import *
from maproomdungeoneastwall import *
from maproombase import *
from northtilebox import *
from southtilebox import *
from westtilebox import *
from easttilebox import *

class MaproomDungeon(MaproomBase):
    "Room with a (big) map"
    def __init__(self,x,y):
        MaproomBase.__init__(self,x,y)
        self.northwalls = []
        self.southwalls = []
        self.westwalls = []
        self.eastwalls= []
        self.gameobjects = []
        self.westtileboxes = []
        self.northtileboxes = []
        self.easttileboxes = []
        self.southtileboxes = []
        self.tileboxes = []
        self.pits = []
        self.exits = []

    def removegameobject(self, o):
	for o2 in self.gameobjects:
		if o2 == o:
			self.gameobjects.remove(o)
       			return
 
    def addnorthwall(self, x,y):
        self.northwalls.append(MaproomDungeonNorthWall(x,y))

    def addsouthwall(self, x,y):
        self.southwalls.append(MaproomDungeonSouthWall(x,y))

    def addwestwall(self, x,y):
        self.westwalls.append(MaproomDungeonWestWall(x,y))

    def addeastwall(self, x,y):
        self.eastwalls.append(MaproomDungeonEastWall(x,y))
       
 
    def addnorthtilebox(self, x,y,w,h,nx,ny,fn):
        self.northtileboxes.append(NorthTilebox(x,y,w,h,nx,ny,fn))

    def addsouthtilebox(self, x,y,w,h,nx,ny,fn):
        self.southtileboxes.append(SouthTilebox(x,y,w,h,nx,ny,fn))

    def addwesttilebox(self, x,y,w,h,nx,ny,fn):
        self.westtileboxes.append(WestTilebox(x,y,w,h,nx,ny,fn))

    def addeasttilebox(self, x,y,w,h,nx,ny,fn):
        self.easttileboxes.append(EastTilebox(x,y,w,h,nx,ny,fn))
       

    def draw(self,game):
        # draw bg
        game.screen.blit(self.background, (self.relativex, self.relativey))
        # draw tileboxes 
        for t in self.tileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        for t in self.northtileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        for t in self.easttileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        for t in self.southtileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        for t in self.westtileboxes:
            t.draw(game.screen,self.relativex,self.relativey)
        # draw walls
        for w in self.northwalls:
            w.draw(game.screen,self.relativex,self.relativey)
        for w in self.southwalls:
            w.draw(game.screen,self.relativex,self.relativey)
        for w in self.westwalls:
            w.draw(game.screen,self.relativex,self.relativey)
        for w in self.eastwalls:
            w.draw(game.screen,self.relativex,self.relativey)
        # draw gameobjects
        for i in self.gameobjects:
	    if i != None:
		i.update(game)
		i.draw(game.screen,self)
        for e in self.exits:
        	if hasattr(e, 'draw'):
            		e.draw(game.screen,self.relativex,self.relativey)
	 
    def collide(self, player):	
	for i in self.gameobjects:
	    if i != None and i.collide(self, player):
		return 2 # 1 kills game
	for w in self.northwalls:
	    if w != None and w.collide(self, player):
		return 2
	for w in self.southwalls:
	    if w != None and w.collide(self, player):
		return 2
	for w in self.westwalls:
	    if w != None and w.collide(self, player):
		return 2
	for w in self.eastwalls:
	    if w != None and w.collide(self, player):
		return 2
	for t in self.northtileboxes:
		if t != None and t.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2 
	for t in self.easttileboxes:
		if t != None and t.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2
	for t in self.southtileboxes:
		if t != None and t.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2 
	for t in self.westtileboxes:
		if t != None and t.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2 
	for p in self.pits:
		if p != None and p.collide(self,player):
			return 2
	for t in self.tileboxes:
		if t != None and t.collide(self,player):
			self.undomove()
	                # FIXME self.undomove()
			return 2 
        for e in self.exits:
	    if e != None and e.collide(self, player):
		return 2 # 1 kills game
	return 0

    def collidewithenemy(self, enemy):
	for t in self.tileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
	for t in self.northtileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
	for t in self.easttileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
	for t in self.southtileboxes:
		if t != None and t.collidewithenemy(self,enemy):
                    enemy.undomove()
                    return 2 # 1 kills game
	for t in self.westtileboxes:
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


    def getclosestgameobject(self, playerx, playery):
	### FIXME closest game object, needs double lists
	minx = 1000
	miny = 1000
	closestgameobject = None
	for go in self.gameobjects:
		if (go and (minx >= math.fabs(go.x-playerx) and 
		    	miny >= math.fabs(go.y-playery))):

			minx = math.fabs(go.x-playerx)
			miny = math.fabs(go.y-playery)
			closestgameobject = go	
	
	return closestgameobject	
