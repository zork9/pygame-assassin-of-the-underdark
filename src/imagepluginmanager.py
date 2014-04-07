
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
import sys
import os

class ImagePluginManager:
    ""
    def __init__(self, directory = "./plugins/"):
	### self.pluginrc = pluginrc
	self.pluginfilenames = []
	self.plugindirectory = directory 
	self.addpluginpathtosyspath()

    def addpluginpathtosyspath(self):
	sys.path.append(self.plugindirectory)

    def filetoimport(self, filename):
	return filename.split('.')[0] ## FIXME .x.py

    def start(self):
	if os.path.isdir(self.plugindirectory):
		self.refresh(self.plugindirectory)
###	if os.path.isdir('./scripts'):
###		self.refresh("./scripts/")

    def getpluginfilenames(self):
	return self.pluginfilenames
	
    def refresh(self, plugindirectory = "./plugins/"):
	filenames = os.listdir(plugindirectory)
	for filename in filenames:
		if filename.endswith(".py"):
			self.pluginfilenames.append(filename)	
     
