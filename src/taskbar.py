
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
from gameobject import *
from inventorybomb import *
from inventorysword import *
from inventoryrubysword import *

class Taskbar:
    "Taskbar"
    def __init__(self, screen, font, player):
        self.screen = screen	
        self.font = font
        self.player = player
        self.background = pygame.image.load('./pics/taskbar-bg.bmp').convert()
        self.background.set_colorkey((0,0,255)) 
        #self.pc = pygame.image.load(player.askpicture()).convert()
        self.swordimage = pygame.image.load('./pics/taskbar-defaultsword1-32x32.bmp').convert()
        self.swordimage.set_colorkey((0,0,255)) 
	self.inventoryitem = None ## InventoryBomb() 
	self.sworditem = InventoryRubySword() ### None or InventorySword() 
	self.spellitem = None ## InventorySpell() 

    def drawlife(self):
	for i in range(0,self.player.hitpoints):
		self.screen.blit(self.lifeimage, (10+i*2,10))

    def draw(self):
        self.screen.blit(self.background, (0, 300))
        self.screen.blit(self.font.render(self.player.askrace() + ' ' + self.player.askclass(), 6, (255,0,0)), (0+70,0+300))
 
        if self.sworditem:
		self.sworditem.draw(self.screen, 180, 310)
        if self.inventoryitem:
		self.inventoryitem.draw(self.screen, 220, 310)
        if self.spellitem:
		self.spellitem.draw(self.screen, 260, 310)
        	self.screen.blit(self.font.render(self.spellitem.name, 6, (255,255,255)), (265,335))

    def setpickup(self, o):
	if o.inventoryitem and o.inventoryitem.typename == "sword":
		self.sworditem = o.inventoryitem
	elif o.inventoryitem and o.inventoryitem.typename == "spell":
		self.spellitem = o.inventoryitem


