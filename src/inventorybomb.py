
# Copyright (C) Johan Ceuppens 2011
# Copyright (C) Johan Ceuppens 2010

# Copyright (C) Johan Ceuppens 2009 
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

from inventoryitem import *
import bomb 

class InventoryBomb(Inventoryitem):
    def __init__(self):
        Inventoryitem.__init__(self, "./pics/bomb-inventory-34x36.bmp")

    def use(self,game):
        game.room.gameobjects.append(bomb.Bomb(game.player.x-game.room.relativex,game.player.y-game.room.relativey))
        print 'You used a bomb' 
