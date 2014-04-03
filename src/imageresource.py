
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
from resourcebase import *
from resourcesubject import *
from imagehandle import *

class ImageResource(ResourceBase,ResourceSubject):
    ""
    def __init__(self):
	ResourceBase.__init__(self)
	ResourceSubject.__init__(self)
	self.imagehandle = None

    def load(self, filename, r,g,b):
	self.loadfile(filename)
    	self.imagehandle.set_colorkey_rgb((r,g,b))

    def load0(self, filename):
	self.loadfile(filename)
    	self.imagehandle.set_colorkey_rgb((0,0,0))
	return self.imagehandle

    def loadfile(self, filename):
    	self.imagehandle = ImageHandle()
	self.surface = self.get_image_surface(filename).convert()
    	self.imagehandle.setimage(self.surface)

    def notify(self):
	for o in self.observers:
		if o != None:
			o.notify()
    def getimage(self):
	if self.imagehandle != None:
		return self.imagehandle.getimage()	
	else:
		return None

##### private functions

    def get_image_surface(self, imgfilename):
	self.filestatus = FileHandle.FILE_OPEN
    	self.surface = pygame.image.load(imgfilename).convert()
	self.filestatus = FileHandle.FILE_CLOSED
	return self.surface

    def set_colorkey_rgb(self, rgb):
    	self.imagehandle.set_colorkey(rgb)

