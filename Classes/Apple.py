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

        self.apples_on_screen = 1
        self.apples = []

        self.place_apple(snake)

    def place_apple(self, snake, snake_collided_with_apple_index: int = None):
        """snake_collided_with_apple_tuple
        this method tries to find a place to put the apple it has a loop so
        it wont stop until it finds it
        :param snake: Snake
        :param snake_collided_with_apple_index: int
        :return: None
        """
        if snake_collided_with_apple_index is None:
            self.apples.clear()
            for i in range(self.apples_on_screen):
                while True:
                    new_apple_loc = [
                        random.randrange(0, self.WIDTH / self.SQ_SIZE) * self.SQ_SIZE,
                        random.randrange(0, self.HEIGHT / self.SQ_SIZE) * self.SQ_SIZE
                    ]

                    if new_apple_loc not in snake.snake_parts and new_apple_loc not in self.apples:
                        self.apples.append(new_apple_loc)
                        break

        elif snake_collided_with_apple_index is not None:
            self.apples.pop(snake_collided_with_apple_index)
            while True:
                new_apple_loc = [
                    random.randrange(0, self.WIDTH / self.SQ_SIZE) * self.SQ_SIZE,
                    random.randrange(0, self.HEIGHT / self.SQ_SIZE) * self.SQ_SIZE
                ]

                if new_apple_loc not in snake.snake_parts and new_apple_loc not in self.apples:
                    self.apples.append(new_apple_loc)
                    break

    def create_new_apple(self, snake):
        """
        it adds a new apple to the screen
        :param snake: Snake
        :return: None
        """
        while True:
            new_apple_loc = [
                random.randrange(0, self.WIDTH / self.SQ_SIZE) * self.SQ_SIZE,
                random.randrange(0, self.HEIGHT / self.SQ_SIZE) * self.SQ_SIZE
            ]

            if new_apple_loc not in snake.snake_parts and new_apple_loc not in self.apples:
                self.apples.append(new_apple_loc)
                break

    def draw(self):
        """
        it draws the apple
        :return:
        """
        for apple in self.apples:
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(apple[0], apple[1], self.width - 3, self.height - 3), 2)
