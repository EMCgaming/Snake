import pygame
from Classes import Game
from Classes import Gui
from Classes import Snake
import numpy as np

# initialize pygame
pygame.init()
pygame.font.init()

# setup window
WIDTH, HEIGHT = 600, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))

# create the board were the info is going to be saved
board = np.zeros((20, 20))

# create class instances/variables
gui = Gui()
snake = Snake()
clock = pygame.time.Clock()
FPS = 60
SQ_SIZE = 20  # how much space will 1 block take up in the screen


# main loop obj
game = Game(WIDTH=WIDTH, HEIGHT=HEIGHT, SQ_SIZE=SQ_SIZE, WIN=WIN, board=board, clock=clock, FPS=FPS, snake=snake, gui=gui)
game.run()
