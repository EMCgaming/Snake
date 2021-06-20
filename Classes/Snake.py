import pygame
import numpy as np


class Snake:
    def __init__(self, WIDTH: int, HEIGHT: int, x: int, y: int, width: int, height: int, WIN: pygame.surface.Surface,
                 SQ_SIZE: int, color: tuple = (255, 0, 0), length: int=4):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.WIN = WIN
        self.SQ_SIZE = SQ_SIZE
        self.color = color

        self.length = length
        self.moving_to = [1, 0]
        self.direction = "right"

        self.snake_parts = []
        self.create_snake()
        for snake_part in self.snake_parts:
            snake_part[0] -= len(self.snake_parts)*SQ_SIZE

    def create_snake(self):
        self.snake_parts = []
        cur_loc = [0, self.SQ_SIZE*((self.HEIGHT/self.SQ_SIZE)/2)]
        shift_amount = 0
        for i in range(self.length):
            self.snake_parts.append([cur_loc[0] + shift_amount, cur_loc[1]])
            shift_amount += self.SQ_SIZE
        self.snake_parts.reverse()

    def draw(self):
        for snake_part in self.snake_parts:
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(snake_part[0], snake_part[1], self.SQ_SIZE - 3, self.SQ_SIZE - 3), 2)

    def event_handler(self, event: pygame.event.Event):
        if event.key == pygame.K_w and not self.direction == "down" or event.key == pygame.K_UP and not self.direction == "down":  # move up
            self.moving_to = [0, 1]
            self.direction = "up"
        elif event.key == pygame.K_s and not self.direction == "up" or event.key == pygame.K_DOWN and not self.direction == "up":  # move down
            self.moving_to = [0, -1]
            self.direction = "down"
        elif event.key == pygame.K_d and not self.direction == "left" or event.key == pygame.K_RIGHT and not self.direction == "left":  # move right
            self.moving_to = [1, 0]
            self.direction = "right"
        elif event.key == pygame.K_a and not self.direction == "right" or event.key == pygame.K_LEFT and not self.direction == "right":  # move left
            self.moving_to = [-1, 0]
            self.direction = "left"

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

    def collide(self, apple):
        if (self.snake_parts[0][0], self.snake_parts[0][1]) == (apple.x, apple.y):
            return True
        return False

    def add_length(self, apple):
        new_head = [apple.x, apple.y]
        self.snake_parts.insert(0, new_head)




