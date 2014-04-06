
# Copyright (C) Johan Ceuppens 2014

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
from stateimageresourcelibrary import *
from imageresource import *

class PlayerMonkResources:
	"Player Monk Resources"
	def __init__(self):
		self.stimlib = Stateimageresourcelibrary()
		imageres = ImageResource().load0('./pics/playermonk1-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk2-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk3-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk2-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk1-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk2-48x48.bmp')
		self.stimlib.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonk3-48x48.bmp')
		self.stimlib.addpicture(imageres)
		self.stimlibfight = Stateimageresourcelibrary()
		imageres = ImageResource().load0('./pics/playermonkfight1-48x48.bmp')
		self.stimlibfight.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonkfight1-48x48.bmp')
		self.stimlibfight.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonkfight2-48x48.bmp')
		self.stimlibfight.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonkfight2-48x48.bmp')
		self.stimlibfight.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonkfight3-48x48.bmp')
		self.stimlibfight.addpicture(imageres)
		imageres = ImageResource().load0('./pics/playermonkfight3-48x48.bmp')
		self.stimlibfight.addpicture(imageres)

	def askpicture(self):
		return './pics/taskbar-PC-fighter.bmp'

