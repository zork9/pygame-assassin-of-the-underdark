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

from selector import *
from taskbar import *
from time import *
from inventory import *
from meter import *
from playergnollfighter import*
from playerhumanfighter import*
from playerkattafighter import*
from playerelffighter import*
from playerdrowfighter import*
from playerdrowmage import *
from bomb import *
from playergnollmagicuser import*
from playerhumanmagicuser import*
from playerkattamagicuser import*
from playerelfmagicuser import*
from playerdrowmagicuser import*

class Game:
    "Main function"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        screen = pygame.display.set_mode((300, 350))
        font = pygame.font.SysFont("Times", 8)
        gameover = 0

        askplayers = 0 # NOTE: 2 Player flag
        
        blankimage = pygame.image.load('./pics/blank.bmp').convert()
        ## There are several title screens in the ./pics/ directory
        titleimage = pygame.image.load('./pics/titlescreen0.3.bmp').convert()
        self.x = 0
        self.y = 0
        
        while gameover == 0:
            pygame.display.update()
            screen.blit(titleimage, (0,0))
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    gameover = 1
                if event.type == pygame.MOUSEBUTTONDOWN:
                    gameover = 1

        self.room = Maproom1(0,0)
        heartmeter = Meter()
###        player = PlayerDrowMage(heartmeter)
        screen.blit(blankimage, (0,0))
        selector = Selector(screen, font)

        selector.select()
        
##	heartmeter = Meter()
##	player = PlayerFighter(heartmeter)default fighter class
	if selector.askrace() == "Human":
            if selector.askclass() == "Fighter":
                player = PlayerHumanFighter(heartmeter)
            elif selector.askclass() == "Magic User":
                player = PlayerHumanMagicuser(heartmeter)
        elif selector.askrace() == "Gnoll":
            if selector.askclass() == "Fighter":
                player = PlayerGnollFighter(heartmeter)
            elif selector.askclass() == "Magic User":
                player = PlayerGnollMagicuser(heartmeter)
        elif selector.askrace() == "Katta":
            if selector.askclass() == "Fighter":
                player = PlayerKattaFighter(heartmeter)
            elif selector.askclass() == "Magic User":
                player = PlayerKattaMagicuser(heartmeter)
        elif selector.askrace() == "Elven":
            if selector.askclass() == "Fighter":
                player = PlayerElfFighter(heartmeter)
            elif selector.askclass() == "Magic User":
                player = PlayerElfMagicuser(heartmeter)
        elif selector.askrace() == "Drow":
            if selector.askclass() == "Fighter":
                player = PlayerDrowFighter(heartmeter)
            elif selector.askclass() == "Magic User":
                player = PlayerDrowMagicuser(heartmeter)
	else: ### default human fighter
                player = PlayerHumanFighter(heartmeter)
##        if selector.askrace() == "Abeille":
##            if selector.askclass() == "Fighter":
##                player = PlayerAbeilleFighter(heartmeter)
        
##        player2 = None
##        
      
        self.inventoryitem = None
        self.inventorymasterkey = None
        self.inventorykey1 = None
        self.inventorykey2 = None
        self.inventoryrubysword = None
        
        self.taskbar = Taskbar(screen,font,player)
        self.talker = None
        
        pygame.key.set_repeat(1,1)
        gameover = 0
        while gameover == 0:

            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
            	    
                    # player 1 key controls
                    player.draw(screen)
                    if event.key == K_x:
                        if self.room.collide(player) == 2:
                            self.talker = self.room.talkto() # FIX
                            print "self.talker=%s" % self.talker
			if self.talker == None:
                        	id = player.pickup(self.room)
				if id == 5:
		                	self.taskbar.setrubysword()
					player.setrubysword()
                    elif event.key == K_z:
                        player.fight(self.room)  
                    elif event.key == K_UP:
                        self.room.movedown()    
                    elif event.key == K_DOWN:
                        self.room.moveup()    
                    elif event.key == K_LEFT:
                        self.room.moveright()    
                    elif event.key == K_RIGHT:
                        self.room.moveleft()    
                    elif event.key == K_SPACE:
                        self.room.gameobjects.append(Bomb(player.x-self.room.relativex,player.y-self.room.relativey))
    
                    elif event.key == K_i:
#                        self.level.gameover = 1
                      #FIXME  pygame.event.flush()
                        flag = 0
                        inventory = Inventory()
		
			##if Scrollinvisibility(0,0,0,0,"1","1").readkeys(None):
                        ##    inventory.additem(Inventoryscrollinvisibility())

			if self.inventorymasterkey == 1:
                       		1###FIX for key in inventory.additem(Inventorymasterkey())
                        if self.inventorykey1 == 1:
                       		1###FIX for key in inventory.additem(Inventorykey1())
                       	if self.inventorykey2 == 1:
                       		1###FIX for key in inventory
        		pygame.key.set_repeat(1000,1000)
			while flag == 0:#NOTE1
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    return

                                elif event.type == KEYDOWN:
                                    if event.key == K_LEFT:
                                        inventory.moveleft()
                                    elif event.key == K_RIGHT:
                                        inventory.moveright()
                                    elif event.key == K_z or event.key == K_x:
                                        self.inventoryitem = inventory.getitem(self.inventoryitem)
					self.taskbar.inventoryitem = self.inventoryitem
					print "%s selected from inventory" % (self.inventoryitem)
                                        flag = 1


                                inventory.draw(screen)
                                pygame.display.update()
 
#	    pickupid = self.room.pickup(player)
#	    if pickupid:
#		if pickupid == 1: # NOTE : masterkey id
#		    self.inventorymasterkey = 1
#		elif pickupid == 2: ## NOTE: dungeonentrance 2 id opens with key 1
 #                   if self.inventorykey1 == 1:
#                        self.room.removeentrance2()
#                elif pickupid == 3: # NOTE dungeon key 1 id
#                    self.inventorykey1 = 1
#                elif pickupid == 4: # NOTE dungeon key 2 id
#                    self.inventorykey2 = 1
#                elif pickupid == 5: # NOTE ruby sword id
#                    self.inventoryrubysword = 1
#                    self.taskbar.setrubysword()
			 
            if self.room.collide(player) == 1 or player.hitpoints <= 0: # NOTE: return 1 after player heartmeter runs out (player.hit)
        	endingimage = pygame.image.load('./pics/endingscreen.bmp').convert()
        	while gameover == 0:
	            	pygame.display.update()
        	    	screen.blit(endingimage, (0,0))
            		for event in pygame.event.get():
                		if event.type == QUIT:
                    			return
                		elif event.type == KEYDOWN:
                    			gameover = 1
					return
                		if event.type == pygame.MOUSEBUTTONDOWN:
                    			gameover = 1
					return
            ###if self.room.collide(player) == 3:###Dungeon wall
                ##self.room.undomove()
            ###    self.room.removeentrance2()

            self.room.draw(screen,player) 
            player.drawstatic(screen)
            
	    sleep(0.2)
            # fight for enemies
            # remove dead game objects

	    ### Set player hitpoints in life bar
	    heartmeter.index = player.hitpoints

            for o in self.room.gameobjects:
                if o:
                    o.fight(self.room,player)
                    if o.hitpoints <= 0:
                        self.room.removeobject(o)

            if self.talker != None:
                self.talker.talk(screen,font)

            self.taskbar.draw()
            ###if self.inventoryitem:
	    ###	self.inventoryitem.draw(screen, 0,0)
            heartmeter.draw(screen)
            
            pygame.display.update()
            screen.blit(blankimage, (0,0))
            roomnumber = self.room.exit(self)
            self.chooseroom(roomnumber,font)


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



