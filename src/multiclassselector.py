
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
from fightermagicuserclassbutton import *
from fighterthiefclassbutton import *
from magicuserthiefclassbutton import *
from fighterclassbutton import *
from magicuserclassbutton import *
from thiefclassbutton import *
import sys

class MultiClassSelector(WidgetRootWindow):
    "Multi Class Selector"
    def __init__(self, screen, font):
	WidgetRootWindow.__init__(self, 300,350, self)

	# construct widgets
	
	self.add_widget(FighterMagicuserClassButton(self, self.selectfightermagicuser, None)) 
	self.add_widget(FighterThiefClassButton(self, self.selectfighterthief, None)) 
	self.add_widget(MagicuserThiefClassButton(self, self.selectmagicuserthief, None)) 
	self.add_widget(FighterClassButton(self, self.selectfighter, None)) 
	self.add_widget(MagicuserClassButton(self, self.selectmagicuser, None)) 
	self.add_widget(ThiefClassButton(self, self.selectthief, None)) 

        self.screen = screen
        self.font = font
        self.background = pygame.image.load('./pics/blank.bmp').convert()
        self.klass = "Random Class"

	self.yoffset = 70

	self.classeslist = ["Fighter", "Magic User", "Thief", "Fighter Magic User", "Fighter Thief", "Magic User Thief"]

        # fighters

        self.fightermagicuserimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.fighterthiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.magicuserthiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.fighterimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.magicuserimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()
        self.thiefimage = pygame.image.load('./pics/playerhumanfighter1-48x48.bmp').convert()


    def selectfightermagicuser(self):
	self.klass = "Fighter Magic User"	

    def selectfighterthief(self):
	self.klass = "Fighter Thief"	

    def selectmagicuserthief(self):
	self.klass = "Magic User Thief"	

    def selectfighter(self):
	self.klass = "Fighter"	

    def selectmagicuser(self):
	self.klass = "Magic User"	

    def selectthief(self):
	self.klass = "Thief"	


	### NOTE draw member func is in rootwindow
    def drawimages(self):
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
        self.screen.blit(self.magicuserimage, (200,0))
        self.screen.blit(self.font.render("magic user", 6, (255,255,255)), (200,50))
        self.screen.blit(self.thiefimage, (250,0))
        self.screen.blit(self.font.render("thief", 6, (255,255,255)), (250,50))





    def select(self):
        while 1:
                self.drawimages()

		# Needs main loop

		self.draw(self.screen)
	
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type == QUIT:
			sys.exit
                        return
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        position = pygame.mouse.get_pos()
                        mousex = position[0]
                        mousey = position[1]

			self.widgetroot.interrupt(pygame.MOUSEBUTTONDOWN, mousex, mousey)

			if self.klass in set(self.classeslist):
				return
			else:
		        	rng = RNG()
		        	class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
		        	self.klass = class0 
		        	return
					
                    if event.type == KEYDOWN:
		        rng = RNG()
		        class0 = self.classeslist[rng.rolldx(len(self.classeslist)-1)]	
		        self.klass = class0 
		        return

    def askclass(self):
        return self.klass


