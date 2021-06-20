import pygame
import numpy as np


class Snake:
    def __init__(self, WIDTH: int, HEIGHT: int, x: int, y: int, width: int, height: int, WIN: pygame.surface.Surface,
                 SQ_SIZE: int, color: tuple = (255, 0, 0), length: int=3):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.WIN = WIN
        self.SQ_SIZE = SQ_SIZE
        self.color = color

        self.snake_parts = [
            [0, SQ_SIZE*15],
            [0 + SQ_SIZE, SQ_SIZE*15],
            [0 + SQ_SIZE + SQ_SIZE, SQ_SIZE*15],
            [0 + SQ_SIZE + SQ_SIZE + SQ_SIZE, SQ_SIZE*15]
        ]

        self.moving_to = [1, 0]

        self.length = length

    def draw(self):
        for snake_part in self.snake_parts:
            pygame.draw.rect(self.WIN, self.color,
                             pygame.Rect(snake_part[0], snake_part[1], self.SQ_SIZE - 3, self.SQ_SIZE - 3), 2)

    def event_handler(self, event: pygame.event.Event):
        if event.key == pygame.K_w or event.key == pygame.K_UP:  # move up
            self.moving_to = [0, 1]
        elif event.key == pygame.K_s or event.key == pygame.K_DOWN:  # move down
            self.moving_to = [0, -1]
        elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:  # move right
            self.moving_to = [1, 0]
        elif event.key == pygame.K_a or event.key == pygame.K_LEFT:  # move left
            self.moving_to = [-1, 0]

    def move(self):
        self.snake_parts.pop(self.snake_parts.index(self.snake_parts[-1]))
        x, y = self.snake_parts[0][0], self.snake_parts[0][1]
        if self.moving_to == [0, 1]:  # move up
            y -= self.SQ_SIZE
        elif self.moving_to == [0, -1]:  # move down
            y += self.SQ_SIZE
        elif self.moving_to == [1, 0]:  # move right
            x += self.SQ_SIZE
        elif self.moving_to == [-1, 0]:  # move left
            x -= self.SQ_SIZE
        self.snake_parts.insert(0, [x, y])
        print(self.snake_parts[0])

