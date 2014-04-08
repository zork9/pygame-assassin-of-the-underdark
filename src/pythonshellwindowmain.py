#!/usr/local/bin/python
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

from maproom1 import *
from maproom2 import *
from maproom3 import *

from rng import *
from pythonshellwindow import *

import imagepluginmanager
import sys,os

class PythonShellWindowMain:
    "Main function of Python shell window"
    def __init__(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((300, 350))
        self.font = pygame.font.SysFont("Times", 8)

        pygame.key.set_repeat(1000,1000)
        #pygame.display.update()
        #self.screen.blit(blankimage, (0,0))
	self.pythonshellwindow = PythonShellWindow(self.screen, self.font)
	self.pythonshellwindow.window_mainloop(0.3)

 
if __name__ == "__main__":
    foo = PythonShellWindowMain()



