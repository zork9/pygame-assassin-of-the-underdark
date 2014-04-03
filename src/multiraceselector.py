
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
import sys

class MultiRaceSelector:
    "Race Selector"
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Fighter"
        self.race = "Human"

	self.yoffset = 70

	self.raceslist = ["Human", "Gnoll", "Katta", "Elf", "Drow"]

        # races 

        self.humanfighterimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.gnollfighterimage = pygame.image.load('./pics/playergnollfighter1-48x48.bmp').convert()
        self.kattafighterimage = pygame.image.load('./pics/playerkattafighter1-48x48.bmp').convert()
        self.elffighterimage = pygame.image.load('./pics/playerelffighter1-48x48.bmp').convert()
        self.drowfighterimage = pygame.image.load('./pics/playerdrowfighter1-48x48.bmp').convert()
###        self.abeillefighterimage = pygame.image.load('./pics/taskbar-PC-abeillefighter.bmp').convert()

    def draw(self):
        # fighters
        self.screen.blit(self.background, (0, 0))       
        self.screen.blit(self.humanfighterimage, (0,0))
        self.screen.blit(self.font.render("human", 6, (255,255,255)), (0,50))
        self.screen.blit(self.gnollfighterimage, (50,0))
        self.screen.blit(self.font.render("gnoll", 6, (255,255,255)), (50,50))
        self.screen.blit(self.kattafighterimage, (100,0))
        self.screen.blit(self.font.render("katta", 6, (255,255,255)), (100,50))
        self.screen.blit(self.elffighterimage, (150,0))
        self.screen.blit(self.font.render("elf", 6, (255,255,255)), (150,50))
        self.screen.blit(self.drowfighterimage, (200,0))
        self.screen.blit(self.font.render("drow", 6, (255,255,255)), (200,50))
###        self.screen.blit(self.abeillefighterimage, (250,0))

    def select(self):
        while 1:
                self.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
			sys.exit
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]
                        
                        if mousex > 0 and mousex < 50 and mousey > 0 and mousey < 50:
                            self.race = "Human"    
                            return
                        elif mousex > 50 and mousex < 100 and mousey > 0 and mousey < 50:
                            self.race = "Gnoll"    
                            return
                        elif mousex > 100 and mousex < 150 and mousey > 0 and mousey < 50:
                            self.race = "Katta"    
                            return
                        elif mousex > 150 and mousex < 200 and mousey > 0 and mousey < 50:
                            self.race = "Elf"    
                            return
                        elif mousex > 200 and mousex < 250 and mousey > 0 and mousey < 50:
                            self.race = "Drow"    
                            return
			else:
				rng = RNG()
				race0 = self.raceslist[rng.rolldx(len(self.raceslist)-1)]	
				self.race = race0 
				return



    def askrace(self):
        return self.race

