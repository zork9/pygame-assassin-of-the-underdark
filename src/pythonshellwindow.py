
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

class PythonShellWindow(MultiSelectorWindow):
    "Python Shell Window"
    def __init__(self, screen, font):
	MultiSelectorWindow.__init__(self, screen, font, 300,350)
	
	# construct widgets
	self.textarea = None	
	self.textareaparser = PythonTextareaParser(self.textarea)
	self.textarea = WidgetPythonShellTextArea(self, self.textareaparser.parse, None, font)
	self.add_widget(self.textarea) 
	self.textareaparser.textarea = self.textarea
	## FIXME 13 == fontsize
	self.add_widget(WidgetTextXYWHLabel(self, None, None, 0,350-14,300,14, font, "Python Shell")) 

	self.prev = ""	
	

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

			# Note that the argument is a HACK with Y = event.key	
			self.widgetroot.interrupt(pygame.KEYDOWN, self.textarea.x+2, event.key)
			
		time.sleep(integratedsleeptime)

    def askclass(self):
        return self.klass


    ### the following is a HACK, use the following lines 
    ### self.textarea = WidgetPythonShellTextArea(self, self.touchtextarea, None, font)
    ### self.widgetroot.interrupt(pygame.KEYDOWN, self.textarea.x+2, event.key)
    ### Note that this callbac function has been abandoned for a real textarea parser
    def touchtextarea(self,X,Y):

	# switch sshifted keyboard commands
	if self.prev == "right shift" or self.prev == "left shift":
		print "text after update=%s =%s= prev=%s=" % (Y, str(pygame.key.name(Y)), self.prev)
		if pygame.key.name(Y) == ';':
			self.textarea.text += ":"		
		elif pygame.key.name(Y) == '9':
			self.textarea.text += "("		
		elif pygame.key.name(Y) == '0':
			self.textarea.text += ")"		
		self.prev = ""
		return 

	if str(pygame.key.name(Y)) == "space":	
		self.textarea.text += " "	
	elif str(pygame.key.name(Y)) == "tab":	
		self.textarea.text += "\t"	
	elif str(pygame.key.name(Y)) == "backspace":
		if len(self.textarea.text) <= 4:
			return	
		else:
			self.textarea.text = self.textarea.text[:-1]	
	elif Y == K_RETURN:
		###print "foo=%s" % self.textarea.text
		if self.textarea.text.endswith("   ") or self.textarea.text.endswith("\n   "):
			eval(self.textarea.text[4:])
			self.textarea.text = ">>> "
			return
		if self.textarea.text.startswith(">>> def "):	
			print "foo=%s" % self.textarea.text
			if self.textarea.text.endswith(":"): 	
				self.textarea.text += "\n   "
			return	
		elif self.textarea.text.endswith(">>> "):	
			return 
		print "foo=%s" % (self.textarea.text.split('\n')[:-1][0])

		### tabulated line, with text after '   '  
		if self.textarea.text.split('\n')[:-1][0].startswith("   "):
			if len(self.textarea.text.split('\n')[:-1][0]) > len("   "):
				self.textarea.text += "\n"
			return	
	else:
		if pygame.key.name(Y) == "right shift" or pygame.key.name(Y) == "left shift":
			self.prev = pygame.key.name(Y) ### NOTE put also in return stataements
		else:	
			self.textarea.text += str(pygame.key.name(Y))	



