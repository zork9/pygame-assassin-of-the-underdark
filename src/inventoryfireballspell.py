
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

from inventoryspell import *
from fireballspelleffect import *
from rng import *

class InventoryFireballSpell(InventorySpell):
    def __init__(self):
        InventorySpell.__init__(self, "./pics/fireballspell-inventory-36x36.bmp")
	self.name = "fireball"
	self.rng = RNG()

    def cast(self,game):
	go = game.room.getclosestgameobject(game.player.x, game.player.y)
	if go:
		go.hitwithspell(game)
		game.room.gameobjects.append(FireballSpellEffect(go.x, go.y))

    def roll(self, game):
	return self.rng.rollfireball()	

