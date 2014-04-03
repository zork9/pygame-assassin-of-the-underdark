
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
from resourcesdatabasesubject import *
from resourcesdatabasebase import *

##############################################
# Base is where the API of the underlying db 
# works, it is inherited not a member
# This is the interface now :
#
#    def instance(self):
#
#    def get(self, key):
#
#    def add(self, key, value):
#
#    def remove(self, key):
#
##############################################

class ResourcesDatabase(ResourcesDatabaseBase, ResourcesDatabaseObserver):
    ""
    def __init__(self):
	ResourcesDatabaseBase.__init__(self)	
	ResourcesDatabaseObserver.__init__(self, self)

