
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

# FIXME needs to be scripted eventually

class ImageBufferResource(ResourceBase,ResourceSubject):
    ""
    def __init__(self):
	ResourceBase.__init__(self)
	ResourceSubject.__init__(self)

    def dither(self, image):  ## image is a surface(
	image.get_buffer()
	1 # FIXME

    def ditherbuffer(self, imagebufferproxy):
	1 # FIXME	
	
    def notify(self):
	for o in self.observers:
		if o != None:
			o.notify()

