import pygame


class Snake:
    def __init__(self, WIDTH: int, HEIGHT: int, width: int, height: int, WIN: pygame.surface.Surface,
                 SQ_SIZE: int, color: tuple = (255, 0, 0), length: int=1):
        """
        Parameters
        ----------

        :param WIDTH: int
        :param HEIGHT: int
        :param width: int
        :param height: int
        :param WIN: pygame.surface.Surface
        :param SQ_SIZE: int
        :param color: tuple = (255, 0, 0)
        :param length: int=1
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
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
        """
        this function creates the snake based on the length and it
        places it on the left mid of the screen
        :return: None
        """
        self.snake_parts = []
        cur_loc = [0, int(self.SQ_SIZE*((self.HEIGHT/self.SQ_SIZE)/2))]
        shift_amount = 0
        for i in range(self.length):
            self.snake_parts.append([cur_loc[0] + shift_amount, cur_loc[1]])
            shift_amount += self.SQ_SIZE
        self.snake_parts.reverse()

    def recreate(self):
        """
        this method sets the snake length to 1 reset the directions
        and then it creates the snake
        :return: None
        """
        self.length = 1
        self.moving_to = [1, 0]
        self.direction = "right"

        self.snake_parts = []
        self.create_snake()
        for snake_part in self.snake_parts:
            snake_part[0] -= len(self.snake_parts)*self.SQ_SIZE

    def draw(self):
        """
        it draws the snake in the screen
        :return:
        """
        for snake_part in self.snake_parts:
            pygame.draw.rect(self.WIN, self.color, pygame.Rect(snake_part[0], snake_part[1], self.SQ_SIZE - 3, self.SQ_SIZE - 3), 2)

    def event_handler(self, event: pygame.event.Event):
        """
        it handles the necessary events for the snake
        :param event: pygame.event.Event
        :return: None
        """
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
        """
        it moves the snake to the direction that the use has chose
        if the length is bigger than 1 then it removes the last parts and adds it to the front
        :return: None
        """
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
        """
        it checks if the head is out of the main board
        :return: bool
        """
        x = self.snake_parts[0][0]
        y = self.snake_parts[0][1]
        if x < 0 or x >= self.WIDTH or y < 0 or y >= self.HEIGHT:
            return True
        return False

    def collide(self, apple_obj):
        """
        it checks for collision between the snake and the apple
        :param apple_obj: Apple
        :return: bool
        """
        for apple in apple_obj.apples:
            if [self.snake_parts[0][0], self.snake_parts[0][1]] == apple:
                return apple_obj.apples.index(apple)
        return False

    def self_collide(self):
        """
        it checks if the snake has collided with itself
        :return: None
        """
        snake_parts = self.snake_parts[:]
        snake_parts.pop(0)
        for snake_part in snake_parts:
            if self.snake_parts[0][0] == snake_part[0] and self.snake_parts[0][1] == snake_part[1]:
                return True
        return False

    def add_length(self, snake_collided_with_apple_index, apple_obj):
        """
        it adds 1 length to the snake
        :param snake_collided_with_apple_index: Apple
        :param apple_obj: Apple
        :return: None
        """
        new_head = [
            apple_obj.apples[snake_collided_with_apple_index][0],  # x
            apple_obj.apples[snake_collided_with_apple_index][1]   # y
        ]
        self.snake_parts.insert(0, new_head)

    def remove_length(self, amount: int):
        for i in range(amount):
            self.snake_parts.pop()




