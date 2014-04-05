
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
from rng import *
from widgettreenode import *
from widgetframe import *
from multiselectorwindow import *

from humanracebutton import *
from gnollracebutton import *
from kattaracebutton import *
from elfracebutton import *
from drowracebutton import *

import sys
import time

class MultiRaceSelector(MultiSelectorWindow):
    "Multi Race Selector"
    def __init__(self, screen, font):
	MultiSelectorWindow.__init__(self, screen, font, 300,350)

	# construct widgets
	
	self.add_widget(HumanRaceButton(self, self.selecthuman, None)) 
	self.add_widget(GnollRaceButton(self, self.selectgnoll, None)) 
	self.add_widget(KattaRaceButton(self, self.selectkatta, None)) 
	self.add_widget(ElfRaceButton(self, self.selectelf, None)) 
	self.add_widget(DrowRaceButton(self, self.selectdrow, None)) 

	self.yoffset = 70

        self.race = "Random Race"

	self.raceslist = ["Human", "Gnoll", "Katta", "Elf", "Drow"]

    def selecthuman(self):
	self.race = "Human"	

    def selectgnoll(self):
	self.race = "Gnoll"	

    def selectkatta(self):
	self.race = "Katta"	

    def selectelf(self):
	self.race = "Elf"	

    def selectdrow(self):
	self.race = "Drow"	

	### NOTE draw member func is in rootwindow
    def drawimages(self):
	MultiSelectorWindow.drawimages(self)
        self.screen.blit(self.font.render("human", 6, (255,255,255)), (0,50))
        self.screen.blit(self.font.render("gnoll", 6, (255,255,255)), (50,50))
        self.screen.blit(self.font.render("katta", 6, (255,255,255)), (100,50))
        self.screen.blit(self.font.render("elf", 6, (255,255,255)), (150,50))
        self.screen.blit(self.font.render("drow", 6, (255,255,255)), (200,50))

    def window_mainloop(self, integratedsleeptime):
        while 1:
                self.drawimages()

		# Needs main loop

		self.draw(self.screen)
	
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
			sys.exit
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]

			self.widgetroot.interrupt(pygame.MOUSEBUTTONDOWN, mousex, mousey)

			if self.race in set(self.raceslist):
				return
			else:
		        	rng = RNG()
		        	race0 = self.raceslist[rng.rolldx(len(self.raceslist)-1)]	
		        	self.race = race0 
		        	return
					
                    if event.type == KEYDOWN:
		        rng = RNG()
		        race0 = self.raceslist[rng.rolldx(len(self.raceslist)-1)]	
		        self.race = race0 
		        return
		time.sleep(integratedsleeptime)

    def askrace(self):
        return self.race


