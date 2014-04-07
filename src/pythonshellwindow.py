
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
from widgettextxywhlabel import *
from widgetpythonshelltextbox import *
from multiselectorwindow import *
import sys
import time

class PythonShellWindow(MultiSelectorWindow):
    "Python Shell Window"
    def __init__(self, screen, font):
	MultiSelectorWindow.__init__(self, screen, font, 300,350)

	# construct widgets
	
	self.textbox = WidgetPythonShellTextBox(self, self.touchtextbox, None, font)
	self.add_widget(self.textbox) 

	## FIXME 13 == fontsize
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,350-14,300,14, font, "Python Shell")) 

    def touchtextbox(self,X,Y):
	if str(pygame.key.name(Y)) == "space":	
		self.textbox.text += " "	
	elif str(pygame.key.name(Y)) == "backspace":
		if len(self.textbox.text) <= 4:
			return	
		else:
			self.textbox.text = self.textbox.text[:-1]	
	elif str(pygame.key.name(Y)) == "return":	
		self.textbox.text += "\n"	
	else:
		self.textbox.text += str(pygame.key.name(Y))	

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
			sys.exit(0)
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]

			self.widgetroot.interrupt(pygame.MOUSEBUTTONDOWN, mousex, mousey)
			return

                    if event.type == KEYDOWN:
		    	if event.key == K_ESCAPE:
				return
	
			self.widgetroot.interrupt(pygame.KEYDOWN, self.textbox.x+2, event.key)
			
		time.sleep(integratedsleeptime)

    def askclass(self):
        return self.klass


