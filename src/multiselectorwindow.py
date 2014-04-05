
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
from gameobject import *
from rng import *
from widgetrootwindow import *

import sys

class MultiSelectorWindow(WidgetRootWindow):
    "Multi Selector Window"
    def __init__(self, screen, font, ww, hh):
	WidgetRootWindow.__init__(self, ww, hh, self)

        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()

	### NOTE draw member func is in rootwindow
    def drawimages(self):
        self.screen.blit(self.background, (0, 0))       

	### FIXME needs timer
    def window_mainloop(self, integratedsleeptime):
	pass

