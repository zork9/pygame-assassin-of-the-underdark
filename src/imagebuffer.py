
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

# FIXME needs to be scripted (eventually)

# the buffer is persistent, pushes self.imagebufer status through image as
# arguments to functions e.g. dither

class ImageBuffer:
    ""
    def __init__(self):
	self.imagebuffer = None

    ### status get and set functions

    def getwidth(self, image):
	return image.get_width()
	
    def getheight(self, image):
	return image.get_height()

    def getbpp(self, image):
	return image.get_bitsize()

    def set(self, image):  ## image is a surface
	self.imagebuffer = image.get_buffer()

    def printimagedata(self,image):
	self.imagebuffer = image.get_buffer()
	print "width=%d\n" % self.getwidth(image)
	print "height=%d\n" % self.getheight(image)
	print "bpp=%d\n" % image.get_bitsize()
	print "bufferlength=%d\n" % self.imagebuffer.length
	print "buffer=%s\n" % self.imagebuffer.raw

    ### image transformation functions
	
    def dither(self, image):  ## image is a surface
	self.imagebuffer = image.get_buffer()

    def ditherbuffer(self, imagebufferproxy):
	1 # FIXME	


    def write(self, image, offset, bufferraw):
	self.imagebuffer = image.get_buffer()
	self.immagebuffer.write(bufferraw, offset)


