
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
from stateimagelibrary import *
from playerkatta import *
from playerfighter import *
from playerfightermagicuser import *
from playerfighterthief import *
from playermagicuser import *
from playermagicuserthief import *
from playerthief import *
from playermonk import *
from playerdruid import *
from playerassassin import *
from playerelf import *
from playergnoll import *
from playerdrow import *
from playerhuman import *
from broadsword import *
	### NOTE FIXME : remove elfresources as default
from playerelfresources import *

class PlayerBase:
    def __init__(self):
	1

class PlayerBase0:
    def __init__(self):
    	PlayerBase0.FIGHTER,PlayerBase0.MAGICUSER,PlayerBase0.THIEF,PlayerBase0.FIGHTERMAGICUSER,PlayerBase0.FIGHTERTHIEF,PlayerBase0.MAGICUSERTHIEF,PlayerBase0.MONK,PlayerBase0.ASSASSIN,PlayerBase0.DRUID = xrange(9)
    	PlayerBase0.ELF,PlayerBase0.GNOLL,PlayerBase0.KATTA,PlayerBase0.HUMAN,PlayerBase0.DROW = xrange(5)

class PlayerBaseRace:
    def __init__(self,PLAYERRACE):
        classByType = {
                PlayerBase0.HUMAN : PlayerHuman,
                PlayerBase0.GNOLL : PlayerGnoll,
                PlayerBase0.KATTA : PlayerKatta,
                PlayerBase0.ELF : PlayerElf,
                PlayerBase0.DROW : PlayerDrow,
        }
        classByType[PLAYERRACE]

class PlayerBaseKlass:
    def __init__(self,PLAYERCLASS):
        classByType2 = {
                PlayerBase0.FIGHTER : PlayerFighter,
                PlayerBase0.FIGHTERMAGICUSER : PlayerFighterMagicuser,
                PlayerBase0.FIGHTERTHIEF : PlayerFighterThief,
                PlayerBase0.MAGICUSER : PlayerMagicuser,
                PlayerBase0.MAGICUSERTHIEF : PlayerMagicuserThief,
                PlayerBase0.THIEF : PlayerThief,
                PlayerBase0.MONK : PlayerMonk,
                PlayerBase0.ASSASSIN : PlayerAssassin,
                PlayerBase0.DRUID : PlayerDruid,
        }
        classByType2[PLAYERCLASS]


	### NOTE FIXME : remove elfresources as default
class PlayerBase(PlayerBase, PlayerBase, PlayerBase0,PlayerBaseRace,PlayerBaseKlass,PlayerElfResources):
    "Player Base"

    PlayerBase.FIGHTER,PlayerBase.MAGICUSER,PlayerBase.THIEF,PlayerBase.FIGHTERMAGICUSER,PlayerBase.FIGHTERTHIEF,PlayerBase.MAGICUSERTHIEF,PlayerBase.MONK,PlayerBase.ASSASSIN,PlayerBase.DRUID = xrange(9)
    PlayerBase.ELF,PlayerBase.GNOLL,PlayerBase.KATTA,PlayerBase.HUMAN,PlayerBase.DROW = xrange(5)

    def __init__(self,PLAYERRACE,PLAYERCLASS):
	PlayerBase0.__init__(self)
	PlayerBaseRace.__init__(self, PLAYERRACE)
	PlayerBaseKlass.__init__(self, PLAYERCLASS)


	### NOTE FIXME : remove elfresources as default
	PlayerElfResources.__init__(self)
	self.klass = "Elf"
	self.race = "Magic User Thief"
	self.heartmeter = None 
	self.sword = BroadSword(0,0)
	self.hitpoints = 78
        self.x = 150 
        self.y = 150 
        self.w = 48 
        self.h = 48
        self.fightcounter = 0
	self.image = None

    def update(self):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.update()
	    self.image = self.stimlibfight.image
            return
        self.stimlib.update()
	self.image = self.stimlib.image
	
    def drawstatic(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
	self.stimlib.drawstatic(screen,self.x,self.y,0)
	
    def draw(self, screen):
        # NOTE
        if self.fightcounter > 0:
            self.fightcounter += 1
            if self.fightcounter > 10:
                self.fightcounter = 0
            self.stimlibfight.draw(screen,self.x,self.y)
            return
        self.stimlib.draw(screen, self.x,self.y)

    def fight(self,game):
        self.fightcounter = 1
	if game.taskbar.sworditem != None: 
        	o = game.room.collidesword(game)
        	if o:
            		game.room.hitwithsword(o, game)
	else: ### hit with bare hands
        	o = game.room.collidebarehands(game)
        	if o:
            		game.room.hitwithbarehands(o)


    def hit(self):
	self.heartmeter.index -= 1 
	if self.heartmeter.index <= 0:
		return 0 #FIXME return 1 for gameover when collision with enemies 
	else:
		return 0	

    def setheartmeter(self, heartmeter):
	self.heartmeter = heartmeter

    def askrace(self):
        return self.race 

    def askclass(self):
        return self.klass

    def setrace(self, r):
       	self.race = r 

    def setclass(self, c):
       	self.klass = c 

    def askpicture(self):
        return './pics/taskbar-PC.bmp'

    def collidewithenemyweapon(self,room,o):
        if o.collide(room,self):
		return self ## NOTE : returns a single collided entity 
		
	return None

    def hitwithenemyweapon(self,damage):
	if damage > 0:
        	self.hitpoints -= damage

    def pickup(self,room):
        o = room.pickup(self)
	return o

    def talkto(self,room):
        o = room.talkto(self)
	return o

    def setrubysword(self):
	self.sword = RubySword(0,0)

    def useitem(self, game):
	1

    def cast(self, game):
	1
