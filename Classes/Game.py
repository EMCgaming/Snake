import pygame
from .Snake import Snake
from .Apple import Apple


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
                 FPS: int, snake: Snake, apple: Apple):
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
        """
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SQ_SIZE = SQ_SIZE
        self.WIN = WIN
        self.clock = clock
        self.FPS = FPS
        self.snake = snake
        self.apple = apple

        self.font = pygame.font.SysFont("comicsans", 70)

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
    
    def draw(self):
        """
        the method that draws everything that is needed
        :return: None
        """
        self.WIN.fill((0, 0, 0))
        for row in range(round(self.WIDTH/self.SQ_SIZE)):
            for column in range(round(self.HEIGHT/self.SQ_SIZE)):
                pygame.draw.rect(self.WIN, (30, 30, 30), pygame.Rect((row*self.SQ_SIZE, column*self.SQ_SIZE, self.SQ_SIZE - 3, self.SQ_SIZE - 3)), 2)

        self.snake.draw()
        self.apple.draw()

        pygame.display.update()

    def collision(self):
        """
        this method checks for collision with the snake and the bound/apple/itself
        :return: None
        """
        if self.snake.collide(self.apple):
            self.snake.add_length(self.apple)
            self.apple.place_apple(self.snake)
            self.score += 1
            pygame.display.set_caption(f"""stored apples: {self.score}""")
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
        score_label = self.font.render(f"""your score: {self.score}""", True, (255, 0, 0))
        self.WIN.blit(score_label, (self.WIDTH/2 - score_label.get_width()/2, self.HEIGHT/2 - score_label.get_height()/2))
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
        self.score = 0
        pygame.display.set_caption(f"""stored apples: {self.score}""")
        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw()
            self.snake.move()
            self.collision()
