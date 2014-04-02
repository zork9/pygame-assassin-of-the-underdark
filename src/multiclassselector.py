
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

class MulticlassSelector:
    "Class and Race Selector"
    def __init__(self, screen, font):
        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Fighter"
        self.race = "Human"

	self.yoffset = 70

	self.raceslist = ["Human", "Gnoll", "Katta", "Elf", "Drow"]
	self.classeslist = ["Fighter", "Magic User", "Thief"]

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
         
        self.humanthiefimage = pygame.image.load('./pics/playerhumanthief1-48x48.bmp').convert()
        self.gnollthiefimage = pygame.image.load('./pics/playergnollthief1-48x48.bmp').convert()
        self.kattathiefimage = pygame.image.load('./pics/playerkattathief1-48x48.bmp').convert()
        self.elfthiefimage = pygame.image.load('./pics/playerelfthief1-48x48.bmp').convert()
        self.drowthiefimage = pygame.image.load('./pics/playerdrowthief1-48x48.bmp').convert()

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
        
        self.screen.blit(self.humanmagicuserimage, (0,self.yoffset))
        self.screen.blit(self.font.render("human magic user", 6, (255,255,255)), (0,50+self.yoffset))
        self.screen.blit(self.gnollmagicuserimage, (50,self.yoffset))
        self.screen.blit(self.font.render("gnoll magic user", 6, (255,255,255)), (50,50+self.yoffset))
        self.screen.blit(self.kattamagicuserimage, (100,self.yoffset))
        self.screen.blit(self.font.render("katta magic user", 6, (255,255,255)), (100,50+self.yoffset))
        self.screen.blit(self.elfmagicuserimage, (150,self.yoffset))
        self.screen.blit(self.font.render("elf magic user", 6, (255,255,255)), (150,50+self.yoffset))
        self.screen.blit(self.drowmagicuserimage, (200,self.yoffset))
        self.screen.blit(self.font.render("drow magic user", 6, (255,255,255)), (200,50+self.yoffset))
       
	# thieves
 
        self.screen.blit(self.humanthiefimage, (0,self.yoffset * 2))
        self.screen.blit(self.font.render("human thief", 6, (255,255,255)), (0,50+self.yoffset * 2))
        self.screen.blit(self.gnollthiefimage, (50,self.yoffset * 2))
        self.screen.blit(self.font.render("gnoll thief", 6, (255,255,255)), (50,50+self.yoffset * 2))
        self.screen.blit(self.kattathiefimage, (100,self.yoffset * 2))
        self.screen.blit(self.font.render("katta thief", 6, (255,255,255)), (100,50+self.yoffset * 2))
        self.screen.blit(self.elfthiefimage, (150,self.yoffset * 2))
        self.screen.blit(self.font.render("elf thief", 6, (255,255,255)), (150,50+self.yoffset * 2))
        self.screen.blit(self.drowthiefimage, (200,self.yoffset * 2))
        self.screen.blit(self.font.render("drow thief", 6, (255,255,255)), (200,50+self.yoffset * 2))


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
                            self.race = "Elf"    
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
                            self.race = "Elf"    
                            self.klass = "Magic User"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > self.yoffset+0 and mousey < self.yoffset+50:
                            self.race = "Drow"    
                            self.klass = "Magic User"
                            return

                        elif mousex > 0 and mousex < 50 and mousey > self.yoffset * 2+0 and mousey < self.yoffset * 2+50:
                            self.race = "Human"    
                            self.klass = "Thief"
                            return
                        elif mousex > 50 and mousex < 100 and mousey > self.yoffset * 2+0 and mousey < self.yoffset * 2+50:
                            self.race = "Gnoll"    
                            self.klass = "Thief"
                            return
                        elif mousex > 100 and mousex < 150 and mousey > self.yoffset * 2+0 and mousey < self.yoffset * 2+50:
                            self.race = "Katta"    
                            self.klass = "Thief"
                            return
                        elif mousex > 150 and mousex < 200 and mousey > self.yoffset * 2+0 and mousey < self.yoffset * 2+50:
                            self.race = "Elf"    
                            self.klass = "Thief"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > self.yoffset * 2+0 and mousey < self.yoffset * 2+50:
                            self.race = "Drow"    
                            self.klass = "Thief"
                            return
			else:
				rng = RNG()

				race0 = self.raceslist[rng.rolldx(len(self.raceslist)-1)]	
				class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
				self.race = race0 
				self.klass = class0 
				return



    def askrace(self):
        return self.race

    def askclass(self):
        return self.klass
