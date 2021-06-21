import pygame
from . import Shop
from . import Snake
from . import Apple


class Game:
    """
    the main loop that runs and handles the game events

    :param WIDTH: int
    :param HEIGHT: int
    :param SQ_SIZE: int
    :param WIN: pygame.surface.Surface
    :param clock: pygame.time.Clock
    :param FPS: int
    :param snake: Snake
    :param apple: Apple
    """
    def __init__(self, WIDTH: int, HEIGHT: int, SQ_SIZE: int, WIN: pygame.surface.Surface, clock: pygame.time.Clock,
                 FPS: int, snake: Snake, apple: Apple, shop: Shop):
        """
        Parameters
        ----------
        :param WIDTH: int
        :param HEIGHT: int
        :param SQ_SIZE: int
        :param WIN: pygame.surface.Surface
        :param clock: pygame.time.Clock
        :param FPS: int
        :param snake: Snake
        :param apple: Apple
        :param shop: Shop
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SQ_SIZE = SQ_SIZE
        self.WIN = WIN
        self.clock = clock
        self.FPS = FPS
        self.original_FPS = FPS
        self.snake = snake
        self.apple = apple
        self.shop = shop

        self.shop_logic = {
            1: "+FPS",
            2: "-FPS",
            3: "more-apples-screen"

        }

        self.font = pygame.font.SysFont("comicsans", 70)

        self.apples_stored = 0
        self.score = 0
        
    def event_handler(self):
        """
        the main method that handles events
        :return: None
        """
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or keys[pygame.K_ESCAPE]:
                pygame.quit()
                quit(-1)
            if event.type == pygame.KEYDOWN:
                self.snake.event_handler(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                is_clicked = self.shop.is_over()
                if is_clicked is not False:
                    if self.shop.upgrades[is_clicked][8] == 1:
                        if self.apples_stored >= self.shop.upgrades[is_clicked][5] * 2:
                            self.snake.remove_length(self.shop.upgrades[is_clicked][5] * 2)
                            self.apples_stored -= self.shop.upgrades[is_clicked][5] * 2
                            self.shop.upgrades[is_clicked][5] += 1
                            pygame.display.set_caption(f"""stored apples: {self.apples_stored}""")
                            self.FPS += 1
                    if self.shop.upgrades[is_clicked][8] == 2:
                        if self.apples_stored >= self.shop.upgrades[is_clicked][5] * 2:
                            self.snake.remove_length(self.shop.upgrades[is_clicked][5] * 2)
                            self.apples_stored -= self.shop.upgrades[is_clicked][5] * 2
                            self.shop.upgrades[is_clicked][5] += 1
                            pygame.display.set_caption(f"""stored apples: {self.apples_stored}""")
                            self.FPS -= 1
                    if self.shop.upgrades[is_clicked][8] == 3:
                        if self.apples_stored >= self.shop.upgrades[is_clicked][5] * 10:
                            self.snake.remove_length(self.shop.upgrades[is_clicked][5] * 10)
                            self.apples_stored -= self.shop.upgrades[is_clicked][5] * 10
                            self.shop.upgrades[is_clicked][5] += 1
                            pygame.display.set_caption(f"""stored apples: {self.apples_stored}""")
                            self.apple.apples_on_screen += 1
                            self.apple.create_new_apple(self.snake)

    def draw(self):
        """
        the method that draws everything that is needed
        :return: None
        """
        self.WIN.fill((0, 0, 0))
        for row in range(round(self.WIDTH/self.SQ_SIZE)):
            for column in range(round(self.HEIGHT/self.SQ_SIZE)):
                pygame.draw.rect(self.WIN, (30, 30, 30), pygame.Rect((row*self.SQ_SIZE, column*self.SQ_SIZE, self.SQ_SIZE - 3, self.SQ_SIZE - 3)), 2)

        self.apple.draw()
        self.snake.draw()
        self.shop.draw()

        pygame.display.update()

    def collision(self):
        """
        this method checks for collision with the snake and the bound/apple/itself
        :return: None
        """
        snake_collided_with_apple_index = self.snake.collide(self.apple)
        if snake_collided_with_apple_index is not False:
            self.snake.add_length(snake_collided_with_apple_index, self.apple)
            self.apple.place_apple(self.snake, snake_collided_with_apple_index)
            self.apples_stored += 1
            self.score += 1
            pygame.display.set_caption(f"""stored apples: {self.apples_stored}""")
        elif self.snake.out_of_bounds():
            self.loss()
        elif self.snake.self_collide():
            self.loss()

    def loss(self):
        """
        this is the method that is called when the user has lost it
        keeps the snake and the apple were it is and it doesnt change it
         :return: None
        """
        apples_stored_label = self.font.render(f"""your score: {self.score}""", True, (255, 0, 0))
        self.WIN.blit(apples_stored_label, (self.WIDTH/2 - apples_stored_label.get_width()/2, self.HEIGHT/2 - apples_stored_label.get_height()/2))
        pygame.display.update()
        while True:
            self.clock.tick(self.FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                    pygame.quit()
                    quit(-1)
                if event.type == pygame.KEYDOWN:
                    self.snake.recreate()
                    self.apple.place_apple(self.snake)
                    self.run()

    def run(self):
        """
        this is the main loop method that is run when the use wants to start/restart the game
        :return:
        """
        self.apples_stored = 0
        pygame.display.set_caption(f"""stored apples: {self.apples_stored}""")
        for upgrade in self.shop.upgrades:
            upgrade[5] = 1
        self.FPS = self.original_FPS
        self.apple.apples_on_screen = 1
        self.apple.place_apple(self.snake)
        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw()
            self.snake.move()
            self.collision()
