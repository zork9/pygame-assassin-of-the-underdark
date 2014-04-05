
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

from widgetsystem import *
from widgettreenode import *

class Widget:
    ""
    def __init__(self, parent, callback = None, widgettreenode = None, widgetsystem = WidgetSystem()):
	self.widgetroot = WidgetRoot()
	self.widgettreenode = widgettreenode ### widget is doubly-linked with node and node with widget
	self.callback = callback
	self.parent = parent

	### each widget contains a widgetroot which has a subtree of the parent of this widget in it
	self.widgetsystem = widgetsystem

    def set_root_widget(self, widget):
	self.widgetroot.widgettree.root = WidgetTreeNode(widget)

    def add_widget(self, widget):
	self.widgetroot.widgettree.add_widget(widget)	

    def setcallback(self, callback):
	self.callback = callback 
