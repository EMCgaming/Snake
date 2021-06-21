import pygame


class Shop:
    def __init__(self, screen_size: tuple, upgrades: list, WIN: pygame.surface.Surface):
        """
        :param screen_size: tuple
        :param upgrades: list[[x, y, width, height, color, sprite=None the same as the width and the height of the button]]
        :param WIN: pygame.surface.Surface
        """
        self.screen_size = screen_size
        self.upgrades = upgrades
        self.WIN = WIN
        self.font = pygame.font.SysFont("comicsans", 30)
        self.cost_font = pygame.font.SysFont("comicsans", 20)

    def draw(self):
        for upgrade in self.upgrades:
            x = upgrade[0]
            y = upgrade[1]
            width = upgrade[2]
            height = upgrade[3]
            color = upgrade[4]
            lvl = upgrade[5]
            cost = upgrade[6]
            text = upgrade[7]

            pygame.draw.rect(self.WIN, color, pygame.Rect(self.screen_size[0] + x, y, width, height))

            for txt in text.split("|||"):
                text_label = self.font.render(txt, True, (255, 0, 0))
                self.WIN.blit(text_label, (x + self.screen_size[0] + 3, y))
                y += text_label.get_height() + 2

            lvl_label = self.font.render(f"""lvl: {str(lvl)}""", True, (255, 0, 0))
            self.WIN.blit(lvl_label, (x + self.screen_size[0] + 3, y))
            y += lvl_label.get_height() + 2
            cost_label = self.cost_font.render(f"""{lvl * cost} apples""", True, (255, 0, 0))
            self.WIN.blit(cost_label, (x + self.screen_size[0] + 3, y))

    def is_over(self):
        x, y = pygame.mouse.get_pos()

        for upgrade in self.upgrades:
            if pygame.Rect(self.screen_size[0] + upgrade[0], upgrade[1], upgrade[2], upgrade[3]).collidepoint(x, y):
                return self.upgrades.index(upgrade)
        return False

