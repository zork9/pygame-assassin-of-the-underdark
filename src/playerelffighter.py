
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
from stateimagelibrary import *
from playerbase import *
from playerelffighterresources import *
from broadsword import *

class PlayerElfFighter(PlayerBase, PlayerElfFighterResources):
    "playerelffighter Magicuser"
    def __init__(self):
        PlayerBase.__init__(self,PlayerBase.ELF,PlayerBase.FIGHTER)
	PlayerElfResources.__init__(self)
	self.sword = BroadSword(0,0)

    def askclass(self):
        return "Fighter"

    def askrace(self):
        return "Elf"

    def askpicture(self):
        return './pics/taskbar-PC-elffighter.bmp'
