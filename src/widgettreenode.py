
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


    def depth_first_search(self, d): ### depth-first search
	for tn in self.nodes:
		if tn.data == d:
			return self
		else:
			tn.search(d)
	return None 

