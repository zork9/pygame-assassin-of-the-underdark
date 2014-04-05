
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

class WidgetTreeNode(TreeNode):
    ""
    def __init__(self, widget = None):
	TreeNode.__init__(self, widget)	
	self.widget = widget ### widget is doubly-linked with node and node with itself 

    def add(self, d):
	self.nodes.add(d)

    def searchXY(self, SIGNAL, X, Y):
	if hasattr(self.widget,'x') and hasattr(self.widget,'y') and hasattr(self.widget, 'w') and hasattr(self.widget, 'h') and X > self.widget.x and X < self.widget.x + self.widget.w and Y > self.widget.y and Y < self.widget.y + self.widget.h:
		if self.nodes == [] or self.nodes == None:
			self.widget.callback() ### NOTE use args 
			return self.widget
	else:
		for tn in self.nodes:
		### FIXME hasattr slow, need dispatch
			if hasattr(tn,'x') and hasattr(tn,'y') and hasattr(tn, 'w') and hasattr(tn, 'h') and X > tn.x and X < tn.x + tn.w and Y > tn.y and Y < tn.y + tn.h:
				if tn.widget and tn.widget.callback:
					self.widget.callback() ### NOTE use args 
					return self.widget
				else:
					return tn.searchXY(SIGNAL, X,Y) 

    def draw(self, screen):
	1 ### stub FIXME
