import pygame
from Classes import Game
from Classes import Gui
from Classes import Snake
import numpy as np

# initialize pygame
pygame.init()
pygame.font.init()

# create class instances/variables
Gui = Gui()
Snake = Snake()
clock = pygame.time.Clock()
FPS = 60


# main loop obj
Game = Game()
Game.run()
