
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

class Selector:
    "Class and Race Selector"
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Fighter"
        self.race = "Human"

        # fighters

        self.humanfighterimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.gnollfighterimage = pygame.image.load('./pics/playergnollfighter1-48x48.bmp').convert()
        self.kattafighterimage = pygame.image.load('./pics/playerkattafighter1-48x48.bmp').convert()
        self.elffighterimage = pygame.image.load('./pics/playerelffighter1-48x48.bmp').convert()
        self.drowfighterimage = pygame.image.load('./pics/playerdrowfighter1-48x48.bmp').convert()
###        self.abeillefighterimage = pygame.image.load('./pics/taskbar-PC-abeillefighter.bmp').convert()

        # magic users
       
        self.humanmagicuserimage = pygame.image.load('./pics/playerhumanmagicuser1-48x48.bmp').convert()
        self.gnollmagicuserimage = pygame.image.load('./pics/playergnollmagicuser1-48x48.bmp').convert()
        self.kattamagicuserimage = pygame.image.load('./pics/playerkattamagicuser1-48x48.bmp').convert()
        self.elfmagicuserimage = pygame.image.load('./pics/playerelfmagicuser1-48x48.bmp').convert()
        self.drowmagicuserimage = pygame.image.load('./pics/playerdrowmagicuser1-48x48.bmp').convert()

        # thieves
         
    def draw(self):
        # fighters
        self.screen.blit(self.background, (0, 300))       
        self.screen.blit(self.humanfighterimage, (0,0))
        self.screen.blit(self.font.render("human fighter", 6, (255,255,255)), (0,50))
        self.screen.blit(self.gnollfighterimage, (50,0))
        self.screen.blit(self.font.render("gnoll fighter", 6, (255,255,255)), (50,50))
        self.screen.blit(self.kattafighterimage, (100,0))
        self.screen.blit(self.font.render("katta fighter", 6, (255,255,255)), (100,50))
        self.screen.blit(self.elffighterimage, (150,0))
        self.screen.blit(self.font.render("elf fighter", 6, (255,255,255)), (150,50))
        self.screen.blit(self.drowfighterimage, (200,0))
        self.screen.blit(self.font.render("drow fighter", 6, (255,255,255)), (200,50))
###        self.screen.blit(self.abeillefighterimage, (250,0))


        # magic users
        
        self.screen.blit(self.humanmagicuserimage, (0,70))
        self.screen.blit(self.font.render("human magic user", 6, (255,255,255)), (0,50+70))
        self.screen.blit(self.gnollmagicuserimage, (50,70))
        self.screen.blit(self.font.render("gnoll magic user", 6, (255,255,255)), (50,50+70))
        self.screen.blit(self.kattamagicuserimage, (100,70))
        self.screen.blit(self.font.render("katta magic user", 6, (255,255,255)), (100,50+70))
        self.screen.blit(self.elfmagicuserimage, (150,70))
        self.screen.blit(self.font.render("elf magic user", 6, (255,255,255)), (150,50+70))
        self.screen.blit(self.drowmagicuserimage, (200,70))
        self.screen.blit(self.font.render("drow magic user", 6, (255,255,255)), (200,50+70))

	self.yoffset = 70


    def select(self):
        while 1:
                self.draw()
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]
                        
                        if mousex > 0 and mousex < 50 and mousey > 0 and mousey < 50:
                            self.race = "Human"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 50 and mousex < 100 and mousey > 0 and mousey < 50:
                            self.race = "Gnoll"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 100 and mousex < 150 and mousey > 0 and mousey < 50:
                            self.race = "Katta"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 150 and mousex < 200 and mousey > 0 and mousey < 50:
                            self.race = "Elven"    
                            self.klass = "Fighter"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > 0 and mousey < 50:
                            self.race = "Drow"    
                            self.klass = "Fighter"
                            return

                        elif mousex > 0 and mousex < 50 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Human"    
                            self.klass = "Magic User"
                            return
                        elif mousex > 50 and mousex < 100 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Gnoll"    
                            self.klass = "Magic User"
                            return
                        elif mousex > 100 and mousex < 150 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Katta"    
                            self.klass = "Magic User"
                            return
                        elif mousex > 150 and mousex < 200 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Elven"    
                            self.klass = "Magic User"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Drow"    
                            self.klass = "Magic User"
                            return

    def askrace(self):
        return self.race

    def askclass(self):
        return self.klass
