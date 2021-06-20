import pygame
import numpy as np
from .Gui import Gui
from .Snake import Snake


class Game:
    def __init__(self, WIDTH: int, HEIGHT: int, SQ_SIZE: int, WIN: pygame.surface.Surface, board: np.ndarray,
                 clock: pygame.time.Clock, FPS: int, snake: Snake, gui: Gui):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SQ_SIZE = SQ_SIZE
        self.WIN = WIN
        self.board = board
        self.clock = clock
        self.FPS = FPS
        self.snake = snake
        self.gui = gui
        
    def event_handler(self):
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit(-1)
            if event.type == pygame.KEYDOWN:
                self.snake.event_handler(event)
    
    def draw(self):
        self.WIN.fill((0, 0, 0))
        self.snake.draw()
        pygame.display.update()

    def run(self):
        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw()
            self.snake.move()

