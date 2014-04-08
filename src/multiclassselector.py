
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
from multiclassselectorbutton import *
from fightermagicuserclassbutton import *
from fighterthiefclassbutton import *
from magicuserthiefclassbutton import *
from fighterclassbutton import *
from magicuserclassbutton import *
from thiefclassbutton import *
from monkclassbutton import *
from assassinclassbutton import *
from druidclassbutton import *
from imageresource import *
from monklabel import *
from widgettextxywhlabel import *

import sys
import time

class MultiClassSelector(MultiSelectorWindow):
    "Multi Class Selector"
    def __init__(self, screen, font):
	MultiSelectorWindow.__init__(self, screen, font, 300,350)

	# construct widgets
	
	self.add_widget(FighterMagicuserClassButton(self, self.selectfightermagicuser, None)) 
	self.add_widget(FighterThiefClassButton(self, self.selectfighterthief, None)) 
	self.add_widget(MagicuserThiefClassButton(self, self.selectmagicuserthief, None)) 
	self.add_widget(FighterClassButton(self, self.selectfighter, None)) 
	self.add_widget(MagicuserClassButton(self, self.selectmagicuser, None)) 
	self.add_widget(ThiefClassButton(self, self.selectthief, None)) 
	self.add_widget(MonkClassButton(self, self.selectmonk, None)) 
	self.add_widget(AssassinClassButton(self, self.selectassassin, None)) 
	self.add_widget(DruidClassButton(self, self.selectdruid, None)) 

	## FIXME 13 == fontsize
	self.add_widget(WidgetTextXYWHLabel(self, self.selectfightermagicuser, None, 0,50,50,13, font, "fighter/magicuser")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectfighterthief, None, 50,50,50,13, font, "fighter/thief")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectmagicuserthief, None, 100,50,50,13, font, "magicuser/thief")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectfighter, None, 150,50,50,13, font, "fighter")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectmagicuser, None, 200,50,50,13, font, "magicuser")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectthief, None, 250,50,50,13, font, "thief")) 
	self.add_widget(MonkLabel(self, self.selectmonk, None, font, "monk")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectassassin, None, 50,100,50,13, font, "assassin")) 
	self.add_widget(WidgetTextXYWHLabel(self, self.selectdruid, None, 100,100,50,13, font, "druid")) 

        self.klass = "Random Class"

	self.yoffset = 70

	self.classeslist = ["Fighter", "Magic User", "Thief", "Fighter Magic User", "Fighter Thief", "Magic User Thief", "Monk", "Assassin", "Druid"]


    def selectfightermagicuser(self,X,y):
	self.klass = "Fighter Magic User"	

    def selectfighterthief(self,X,y):
	self.klass = "Fighter Thief"	

    def selectmagicuserthief(self,X,y):
	self.klass = "Magic User Thief"	

    def selectfighter(self,X,y):
	self.klass = "Fighter"	

    def selectmagicuser(self,X,y):
	self.klass = "Magic User"	

    def selectthief(self,X,y):
	self.klass = "Thief"	

    def selectmonk(self,X,y):
	self.klass = "Monk"	

    def selectassassin(self,X,y):
	self.klass = "Assassin"	

    def selectdruid(self,X,y):
	self.klass = "Druid"	

	### NOTE draw member func is in rootwindow
    def drawimages(self):
        MultiSelectorWindow.drawimages(self)       

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

			if self.klass in set(self.classeslist):
				return
			else:
		        	rng = RNG()
		        	class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
		        	self.klass = class0 
		        	return
					
                    if event.type == KEYDOWN:
		        rng = RNG()
		        class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
		        self.klass = class0 
		        return
		time.sleep(integratedsleeptime)

    def askclass(self):
        return self.klass


