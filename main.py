import pygame
from Classes import Game
from Classes import Snake
from Classes import Apple

# initialize pygame
pygame.init()
pygame.font.init()

# setup window
WIDTH, HEIGHT, EXTRA_WIDTH = 600, 600, 100
WIN = pygame.display.set_mode((WIDTH + EXTRA_WIDTH, HEIGHT))

# create class instances/variables
SQ_SIZE = 20  # how much space will 1 block take up in the screen
snake = Snake(WIDTH=WIDTH, HEIGHT=HEIGHT, width=SQ_SIZE, height=SQ_SIZE, WIN=WIN, SQ_SIZE=SQ_SIZE)
apple = Apple(SQ_SIZE=SQ_SIZE, WIDTH=WIDTH, HEIGHT=HEIGHT, width=SQ_SIZE, height=SQ_SIZE, WIN=WIN, snake=snake)
clock = pygame.time.Clock()
FPS = 12


# main loop obj
game = Game(WIDTH=WIDTH, HEIGHT=HEIGHT, SQ_SIZE=SQ_SIZE, WIN=WIN, clock=clock, FPS=FPS, snake=snake,
            apple=apple)
game.run()
