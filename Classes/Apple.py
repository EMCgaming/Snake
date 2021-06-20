import pygame
import random


class Apple:
    def __init__(self, SQ_SIZE: int, WIDTH: int, HEIGHT: int, width: int, height: int, WIN: pygame.surface.Surface,
                 color: tuple=(0, 255, 0)):
        self.SQ_SIZE = SQ_SIZE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.width = width
        self.height = height
        self.WIN = WIN
        self.color = color
        self.x = 0
        self.y = 0
        self.place_apple()

    def place_apple(self):
        self.x = random.randrange(0, self.WIDTH/self.SQ_SIZE)*self.SQ_SIZE
        self.y = random.randrange(0, self.HEIGHT/self.SQ_SIZE)*self.SQ_SIZE

    def draw(self):
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.width - 3, self.height - 3), 2)
