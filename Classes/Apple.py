import pygame
import random
from .Snake import Snake


class Apple:
    def __init__(self, SQ_SIZE: int, WIDTH: int, HEIGHT: int, width: int, height: int, WIN: pygame.surface.Surface,
                 snake: Snake, color: tuple = (0, 255, 0)):
        """
        Parameters
        ----------

        :param SQ_SIZE: int
        :param WIDTH: int
        :param HEIGHT: int
        :param width: int
        :param height: int
        :param WIN: pygame.surface.Surface
        :param snake: Snake
        :param color: tuple = (int, int, int)
        """
        self.SQ_SIZE = SQ_SIZE
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.width = width
        self.height = height
        self.WIN = WIN
        self.color = color
        self.x = 0
        self.y = 0
        self.place_apple(snake)

    def place_apple(self, snake):
        """
        this method tries to find a place to put the apple it has a loop so
        it wont stop until it finds it
        :return: None
        """
        while True:
            x = random.randrange(0, self.WIDTH / self.SQ_SIZE) * self.SQ_SIZE
            y = random.randrange(0, self.HEIGHT / self.SQ_SIZE) * self.SQ_SIZE

            if not [x, y] in snake.snake_parts:
                self.x = x
                self.y = y
                return

    def draw(self):
        """
        it draws the apple
        :return:
        """
        pygame.draw.rect(self.WIN, self.color, pygame.Rect(self.x, self.y, self.width - 3, self.height - 3), 2)
