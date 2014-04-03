
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
from widgettreenode import *
from widgetframe import *
from widgetrootwindow import *
from multiclassselectorbutton import *
import sys

class MultiClassSelector(WidgetRootWindow, WidgetFrame):
    "Multi Class Selector"
    def __init__(self, screen, font):
	WidgetFrame.__init__(self, 0, 0, 300, 350)
	WidgetRootWindow.__init__(self, self)

        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Magic User Thief"
        self.race = "Human"

	self.yoffset = 70

	self.classeslist = ["Fighter Magic User", "Fighter Thief", "Magic User Thief"]

        # fighters

        self.fightermagicuserimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.fighterthiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.magicuserthiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.fighterimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.magicuserimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.thiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()

	self.widgettreenode = WidgetTreeNode()	
	self.button1 = MultiClassSelectorButton(self, None, self.widgettreenode)
	self.widgetsystem.add_widget(self.button1) 
	self.widgettreenode.widget = self.button1 ### NOTE doubly-linked 

    def draw(self):
        # fighters
        self.screen.blit(self.background, (0, 0))       
        self.screen.blit(self.fightermagicuserimage, (0,0))
        self.screen.blit(self.font.render("fighter/magicuser", 6, (255,255,255)), (0,50))
        self.screen.blit(self.fighterthiefimage, (50,0))
        self.screen.blit(self.font.render("fighter/thief", 6, (255,255,255)), (50,50))
        self.screen.blit(self.magicuserthiefimage, (100,0))
        self.screen.blit(self.font.render("magicuser/thief", 6, (255,255,255)), (100,50))
        self.screen.blit(self.fighterimage, (150,0))
        self.screen.blit(self.font.render("fighter", 6, (255,255,255)), (150,50))
        self.screen.blit(self.magicuserthiefimage, (200,0))
        self.screen.blit(self.font.render("magic user", 6, (255,255,255)), (200,50))
        self.screen.blit(self.magicuserthiefimage, (250,0))
        self.screen.blit(self.font.render("thief", 6, (255,255,255)), (250,50))

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
                            self.klass = "Fighter Magic User"
                            return
                        elif mousex > 50 and mousex < 100 and mousey > 0 and mousey < 50:
                            self.klass = "Fighter Thief"
                            return
                        elif mousex > 100 and mousex < 150 and mousey > 0 and mousey < 50:
                            self.klass = "Magic User Thief"
                            return
                        elif mousex > 150 and mousex < 200 and mousey > 0 and mousey < 50:
                            self.klass = "Fighter"
                            return
                        elif mousex > 200 and mousex < 250 and mousey > 0 and mousey < 50:
                            self.klass = "Magic User"
                            return
                        elif mousex > 250 and mousex < 300 and mousey > 0 and mousey < 50:
                            self.klass = "Thief"
                            return
			else:
				rng = RNG()
				class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
				###self.race = race0 
				self.klass = class0 
				return



    def askrace(self):
        return self.race

    def askclass(self):
        return self.klass
