
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
from rng import *
from widgettreenode import *
from widgetframe import *
from widgettextxywhlabel import *
from widgetpythonshelltextbox import *
from multiselectorwindow import *
from pythontextareaparser import *
import sys
import time

class CharacterSheetWindow(MultiSelectorWindow):
    "Python Shell Window"
    def __init__(self, screen, font, player):
	MultiSelectorWindow.__init__(self, screen, font, 300,350)
	
	# construct widgets
	## FIXME 13 == fontsize
	# left widgets
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,0,100,14, font, "Strength")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 100,0,100,14, font, "   " + str(player.strength))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,20,100,14, font, "Intelligence")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 100,20,100,14, font, "   " + str(player.intelligence))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,40,100,14, font, "Agility")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 100,40,100,14, font, "   " + str(player.agility))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,60,100,14, font, "Vitality")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 100,60,100,14, font, "   " + str(player.vitality))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,80,100,14, font, "Luck")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 100,80,100,14, font, "   " + str(player.luck))) 

	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,0,100,14, font, "Weapon Use")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,0,100,14, font, "   " + str(player.weaponuse))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,20,100,14, font, "Parry")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,20,100,14, font, "   " + str(player.parry))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,40,100,14, font, "Dodge")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,40,100,14, font, "   " + str(player.dodge))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,60,100,14, font, "Stealth")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,60,100,14, font, "   " + str(player.stealth))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,80,100,14, font, "Pick Locks")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,80,100,14, font, "   " + str(player.picklocks))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,100,100,14, font, "Throwing")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,100,100,14, font, "   " + str(player.throwing))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,120,100,14, font, "Climbing")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,120,100,14, font, "   " + str(player.climbing))) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 150,140,100,14, font, "Magic")) 
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 250,140,100,14, font, "   " + str(player.magic))) 

    ### NOTE draw member func is in rootwindow
    def drawimages(self):
        MultiSelectorWindow.drawimages(self)       


    def window_mainloop(self, integratedsleeptime):
        while 1:
                self.drawimages()

		self.draw(self.screen)
	
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
			sys.exit(0)
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]

			####self.widgetroot.interrupt(pygame.MOUSEBUTTONDOWN, mousex, mousey)
			return

                    if event.type == KEYDOWN:
		    	###if event.key == K_ESCAPE:
			###	return
			return

			# Note that the argument is a HACK with Y = event.key	
			####self.widgetroot.interrupt(pygame.KEYDOWN, self.textarea.x+2, event.key)
			
		time.sleep(integratedsleeptime)

    def askclass(self):
        return self.klass



