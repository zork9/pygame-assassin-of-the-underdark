
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
import re

class PythonTextareaParser:
    "Python Shell Window Formatting parser"
    def __init__(self,textarea):
	self.prev = ""
	self.textarea = textarea
    ### the following is a HACK, use the following lines 
    ### self.textarea = WidgetPythonShellTextArea(self, self.touchtextbox, None, font)
    ### self.widgetroot.interrupt(pygame.KEYDOWN, self.textbox.x+2, event.key)
    ### Note that this callbac function has been abandoned for a real textarea parser
    ### Note that the argument is a HACK with Y = event.key	

    def parse(self,X,Y):

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
		if self.textarea.text.endswith("\n"):
			exp = ""
			txt = self.textarea.text[4:] 
			for l in self.textarea.lines:
				l = l[3:]
				exp += l
				exp += "\n"
				print "exp=%s" % exp 
			eval(exp)
			self.textarea.text = ">>> "
			return
		elif self.textarea.text.startswith(">>> def "):	
			print "foo=%s" % self.textarea.text
			if self.textarea.text.endswith(":"): 	
				self.textarea.text += "\n..."
			elif self.textarea.lines[-1] != "...":
				self.textarea.text += "\n..."
				return
					
					
		elif self.textarea.text.endswith(">>> "):	
			return 

	else:
		if pygame.key.name(Y) == "right shift" or pygame.key.name(Y) == "left shift":
			self.prev = pygame.key.name(Y)
		else:	
			self.textarea.text += str(pygame.key.name(Y))	



