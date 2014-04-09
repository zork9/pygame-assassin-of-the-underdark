
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
from meter import *

class Mana:
	def __init__(self):
        	self.image = pygame.image.load('./pics/mana3.bmp').convert()
        	self.image.set_colorkey((0,0,0)) 
		

class ManaMeter(Meter):
    "mana meter"
    def __init__(self):
	Meter.__init__(self)
	self.max = 50 
	self.index = 50
	self.picslist = []
	for i in range(0,3):
		self.picslist.append(Mana())
 
    def draw(self,screen):
	# KLUDGY
	j = 0
	for i in range(0,self.index):
        	screen.blit(self.picslist[0].image, (78+j*1, 327+8))
		j += 1
