
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

from treenode import *
from widget import *
from widgetframe import *

class WidgetTextBox(Widget, WidgetFrame):
    ""
    def __init__(self, parent, callback, widgettreenode, font):
	Widget.__init__(self, parent, callback, widgettreenode)	
	WidgetFrame.__init__(self, parent.x, parent.y, parent.w, parent.h)	
	self.font = font 
	self.text = ""

    def draw(self, screen):
        screen.blit(self.font.render(self.text, 8, (255,255,255)), (self.x,self.y))
    		 
