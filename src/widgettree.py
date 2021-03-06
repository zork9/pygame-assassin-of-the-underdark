
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

from tree import *
from widgettreenode import *

class WidgetTree(Tree):
    ""
    def __init__(self):
	Tree.__init__(self)	

    def searchXY(self, SIGNAL, X, Y):
	if self.root and self.root.nodes:
		for tn in self.root.nodes:
			w = tn.searchXY(SIGNAL, X, Y)
			if w != None:
				return w 
	else:
		print "self.root = nil"

    def add_widget(self, widget):
	self.insertnode(WidgetTreeNode(widget))

    def insertnode(self, node):
	self.root.nodes.append(node)	
