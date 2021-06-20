import pygame
from .Gui import Gui
from .Snake import Snake
from .Apple import Apple


class Game:
    def __init__(self, WIDTH: int, HEIGHT: int, SQ_SIZE: int, WIN: pygame.surface.Surface, clock: pygame.time.Clock,
                 FPS: int, snake: Snake, gui: Gui, apple: Apple):
        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT
        self.SQ_SIZE = SQ_SIZE
        self.WIN = WIN
        self.clock = clock
        self.FPS = FPS
        self.snake = snake
        self.gui = gui
        self.apple = apple

        self.font = pygame.font.SysFont("comicsans", 70)

        self.score = 0
        
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
        self.apple.draw()
        pygame.display.update()

    def collision(self):
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

            score_label = self.font.render(f"""your score: {self.score}""", True, (255, 0, 0))
            self.WIN.blit(score_label, (self.WIDTH/2 - score_label.get_width()/2, self.HEIGHT/2 - score_label.get_height()/2))
            pygame.display.update()

    def run(self):
        self.score = 0
        pygame.display.set_caption(f"""stored apples: {self.score}""")
        while True:
            self.clock.tick(self.FPS)
            self.event_handler()
            self.draw()
            self.snake.move()
            self.collision()

