#!/usr/local/bin/python
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

from maproom1 import *
from maproom2 import *

from rng import *
from multiraceselector import *
from multiclassselector import *
from selector import *
from taskbar import *
from time import *
from inventory import *
from meter import *
from playergnollfighter import *
from playerhumanfighter import *
from playerhumanfightermagicuser import *
from playerhumanfighterthief import *
from playerhumanmagicuserthief import *
from playerkattafighter import *
from playerkattafightermagicuser import *
from playerkattafighterthief import *
from playerkattamagicuserthief import *
from playerelffighter import *
from playerdrowfighter import *
from playerdrowmage import *
from bomb import *
from playergnollmagicuser import *
from playergnollfightermagicuser import *
from playergnollfighterthief import *
from playergnollmagicuserthief import *
from playerhumanmagicuser import *
from playerkattamagicuser import *
from playerelfmagicuser import *
from playerdrowmagicuser import *
from playergnollthief import *
from playerhumanthief import *
from playerkattathief import *
from playerelfthief import *
from playerelfmagicuser import *
from playerelffightermagicuser import *
from playerelffighterthief import *
from playerelfmagicuserthief import *
from playerdrowthief import *
from playerdrowfightermagicuser import *
from playerdrowfighterthief import *
from playerdrowmagicuserthief import *

class Game:
    "Main function"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((300, 350))
        self.font = pygame.font.SysFont("Times", 8)
        gameover = 0

        askplayers = 0 # NOTE: 2 Player flag
        
        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        titleimage = pygame.image.load('./pics/titlescreen0.3.bmp').convert()
        self.x = 0
        self.y = 0
        
        while gameover == 0:
            pygame.display.update()
            self.screen.blit(titleimage, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

        self.room = Maproom1(0,0)
        self.heartmeter = Meter()
	self.player = None ### PlayerDrowMage(self.heartmeter)
###self.player = PlayerFighter(self.heartmeter)default fighter class
        self.screen.blit(blankimage, (0,0))

	# display multiclass selection screen and wait for mouse click choice

        self.selectormc = MultiClassSelector(self.screen, self.font)

        self.selectormc.select()



        self.selectormr = MultiRaceSelector(self.screen, self.font)

	# display character selection screen and wait for mouse click choice

        self.selectormr.select()
       
	# get data from character selector screen 

	if self.selectormr.askrace() == "Human":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerHumanFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerHumanMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerHumanThief()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerHumanFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerHumanFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerHumanMagicuserThief()
        elif self.selectormr.askrace() == "Gnoll":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerGnollFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerGnollMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerGnollThief()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerGnollFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerGnollFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerGnollMagicuserThief()
        elif self.selectormr.askrace() == "Katta":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerKattaFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerKattaMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerKattaThief()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerKattaFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerKattaFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerKattaMagicuserThief()
        elif self.selectormr.askrace() == "Elf":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerElfFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerElfMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerElfThief()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerElfFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerElfFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerElfMagicuserThief()
        elif self.selectormr.askrace() == "Drow":
            if self.selectormc.askclass() == "Fighter":
                self.player = PlayerDrowFighter()
            elif self.selectormc.askclass() == "Magic User":
                self.player = PlayerDrowMagicuser()
            elif self.selectormc.askclass() == "Thief":
                self.player = PlayerDrowThief()
            elif self.selectormc.askclass() == "Fighter Magic User":
                self.player = PlayerDrowFighterMagicuser()
            elif self.selectormc.askclass() == "Fighter Thief":
                self.player = PlayerDrowFighterThief()
            elif self.selectormc.askclass() == "Magic User Thief":
                self.player = PlayerDrowMagicuserThief()

##        if self.selectormr.askrace() == "Abeille":
##            if self.selectormc.askclass() == "Fighter":
##                self.player = PlayerAbeilleFighter()

	### print "race=%s class=%s" % (self.selectormr.askrace(),self.selectormc.askclass())
	### KLUDGE, above player ctors must set class and race
	self.player.setrace(self.selectormr.askrace())
	self.player.setclass(self.selectormc.askclass())

	self.player.setheartmeter(self.heartmeter)        
        self.inventory = Inventory()

        self.inventoryitem = None
        self.inventorymasterkey = None
        self.inventorykey1 = None
        self.inventorykey2 = None
        self.inventoryrubysword = None
        
        self.taskbar = Taskbar(self.screen,self.font,self.player)
        self.talker = None
        
        pygame.key.set_repeat(90,90)
        gameover = 0
        while gameover == 0:

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
            	    
                    # player 1 key controls
                    self.player.draw(self.screen)
                    if event.key == K_x:
                        ###if self.room.collide(self.player) == 2:
                        ###    self.talker = self.room.talkto() # FIX
                        ###    print "self.talker=%s" % self.talker
			###if self.talker == None:
                        o = self.player.pickup(self.room)
		        if o != None:
				if o.inventoryitem and o.inventoryitem.typename == "sword":
					self.taskbar.sworditem = o.inventoryitem
				elif o.inventoryitem and o.inventoryitem.typename == "spell":
					self.taskbar.spellitem = o.inventoryitem
				elif o.inventoryitem and o.inventoryitem.typename == "enemy":
					self.inventory.additem(o.inventoryitem)
				elif o.inventoryitem and o.inventoryitem.typename == "inventoryitem":
					self.inventory.additem(o.inventoryitem)
				self.room.removegameobject(o)

	            elif event.key == K_z:
                        self.player.fight(self)  
                    elif event.key == K_UP:
                        self.room.movedown()    
                    elif event.key == K_DOWN:
                        self.room.moveup()    
                    elif event.key == K_LEFT:
                        self.room.moveright()    
                    elif event.key == K_RIGHT:
                        self.room.moveleft()    
                    elif event.key == K_SPACE:
                        self.room.gameobjects.append(Bomb(self.player.x-self.room.relativex,self.player.y-self.room.relativey))
    
                    elif event.key == K_i:
#                        self.level.gameover = 1
                        flag = 0
		
        		pygame.key.set_repeat(1000,1000)
			while flag == 0:#NOTE1
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        self.inventory.moveleft()
                                    elif event.key == K_RIGHT:
                                        self.inventory.moveright()
                                    elif event.key == K_z or event.key == K_x:
                                        self.inventoryitem = self.inventory.getitem(self.inventoryitem)
					self.taskbar.inventoryitem = self.inventoryitem
					print "%s selected from inventory" % (self.inventoryitem)
                                        flag = 1


                                self.inventory.draw(self.screen)
                                pygame.display.update()
                    ### pygame.key.set_repeat(90,90)
 
            if self.room.collide(self.player) == 1 or self.player.hitpoints <= 0: # NOTE: return 1 after player heartmeter runs out (self.player.hit)
        	endingimage = pygame.image.load('./pics/endingscreen.bmp').convert()
        	while gameover == 0:
	            	pygame.display.update()
        	    	self.screen.blit(endingimage, (0,0))
            		for event in pygame.event.get():
                		if event.type == QUIT:
                    			return
                		elif event.type == KEYDOWN:
                    			gameover = 1
					return
                		if event.type == pygame.MOUSEBUTTONDOWN:
                    			gameover = 1
					return
            ###if self.room.collide(self.player) == 3:###Dungeon wall
                ##self.room.undomove()
            ###    self.room.removeentrance2()

            self.room.draw(self) 
            self.player.drawstatic(self.screen)
            
	    sleep(0.09)
            # fight for enemies
            # remove dead game objects

	    ### Set player hitpoints in life bar
	    self.heartmeter.index = self.player.hitpoints

            for o in self.room.gameobjects:
                if o:
                    o.fight(self.room,self.player)
                    if o.hitpoints <= 0:
                        self.room.removeobject(o)

            if self.talker != None:
                self.talker.talk(self.screen,self.font)

            self.taskbar.draw()
            ###if self.inventoryitem:
	    ###	self.inventoryitem.draw(self.screen, 0,0)
            self.heartmeter.draw(self.screen)
            
            pygame.display.update()
            self.screen.blit(blankimage, (0,0))
            roomnumber = self.room.exit(self)
            self.chooseroom(roomnumber,self.font)


    def sethitf(self, hitf):
        for i in self.room.gameobjects:
            i.hitf = hitf

    def setxy(self,xx,yy):
        self.x = xx
        self.y = yy

    def chooseroom(self, roomnumber,font):
        if (roomnumber == 0):
            return
        # NOTE: 1_X  woods around haunted castle
        elif (roomnumber == 1):
            self.talker = None
            self.room = Maproom1(self.x,self.y)
        elif (roomnumber == 1.1):
            self.talker = None
            self.room = Maproom1_1(self.x,self.y)
        elif (roomnumber == 1.2):
            self.talker = None
            self.room = Maproom1_2(self.x,self.y)
        elif (roomnumber == 1.3):
            self.talker = None
            self.room = Maproominn1_3(self.x,self.y)
        elif (roomnumber == 1.4):
            self.talker = None
            self.room = Maproominn1_4(self.x,self.y)
        elif (roomnumber == 1.5):
            self.talker = None
            self.room = Maproominn1_5(self.x,self.y)
        elif (roomnumber == 1.6):
            self.talker = None
            self.room = Maproominn1_6(self.x,self.y)
        # NOTE left woods of haunted castle
        elif (roomnumber == "1.1.1"):
            self.talker = None
            self.room = Maproom1_1_1(self.x,self.y)
        # rooms of haunted castle    
        elif (roomnumber == 2):
            self.talker = None
            self.room = Maproom2(self.x,self.y)
        elif (roomnumber == 3):
            self.talker = None
            self.room = Maproom3(self.x,self.y)
        elif (roomnumber == 4):
            self.talker = None
            self.room = Maproom4(self.x,self.y)
        elif (roomnumber == 5):
            self.talker = None
            self.room = Maproom5(self.x,self.y)
        elif (roomnumber == 6):
            self.talker = None
            self.room = Maproom6(self.x,self.y)
        elif (roomnumber == 7):
            self.talker = None
            self.room = Maproom7(self.x,self.y)
        elif (roomnumber == 8):
            self.talker = None
            self.room = Maproom8(self.x,self.y)
        elif (roomnumber == 9):
            self.talker = None
            self.room = Maproom9(self.x,self.y)
        elif (roomnumber == 10):
            self.talker = None
            self.room = Maproom10(self.x,self.y)
        elif (roomnumber == 11):
            self.talker = None
            self.room = Maproom11(self.x,self.y)
        elif (roomnumber == 12):
            self.talker = None
            self.room = Maproom12(self.x,self.y)
        elif (roomnumber == 13):
            self.talker = None
            self.room = Maproom13(self.x,self.y)
        elif (roomnumber == 14):
            self.talker = None
            self.room = Maproom14(self.x,self.y)
        # set sword parameters
        if self.inventoryrubysword:
            self.sethitf(self.room.gameobjects.hit2)
            
if __name__ == "__main__":
    foo = Game()



