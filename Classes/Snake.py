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

        self.snake_parts = []
        cur_loc = [0, SQ_SIZE*((HEIGHT/SQ_SIZE)/2)]
        shift_amount = 0
        for i in range(length):
            self.snake_parts.append([cur_loc[0] + shift_amount, cur_loc[1]])
            shift_amount += SQ_SIZE
        self.snake_parts.reverse()

        self.moving_to = [1, 0]
        self.length = length

    def draw(self):
        for snake_part in self.snake_parts:
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(snake_part[0], snake_part[1], self.SQ_SIZE - 3, self.SQ_SIZE - 3), 2)

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
        # if the snake size is more than 1
        if len(self.snake_parts) > 1:
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
        # if the length of the snake is 1
        else:
            temp_snake_part = self.snake_parts[0]
            self.snake_parts.pop(self.snake_parts.index(self.snake_parts[-1]))
            x, y = temp_snake_part[0], temp_snake_part[1]
            if self.moving_to == [0, 1]:  # move up
                y -= self.SQ_SIZE
            elif self.moving_to == [0, -1]:  # move down
                y += self.SQ_SIZE
            elif self.moving_to == [1, 0]:  # move right
                x += self.SQ_SIZE
            elif self.moving_to == [-1, 0]:  # move left
                x -= self.SQ_SIZE
            self.snake_parts.insert(0, [x, y])

    def out_of_bounds(self):
        x = self.snake_parts[0][0]
        y = self.snake_parts[0][1]
        if x < 0 or x >= self.WIDTH or y < 0 or y >= self.HEIGHT:
            return True
        return False
