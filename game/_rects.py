import pygame as pg
import _state as st


class Board:

    def __init__(self, screen, settings):

        self.screen = screen

        # Creates a rect containing the board background image
        self.image = pg.image.load('game_images/boards/' + settings.bg_image)
        self.rect = self.image.get_rect()

        # Sets "center" x and y positions to the same as that of the entire viewing screen
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.centery = self.screen.get_rect().centery

    def blitme(self):

        self.screen.blit(self.image, self.rect)


class Token:

    def __init__(self, screen, team, x, y):

        self.screen = screen

        self.team = team
        if self.team == "B":
            self.image = pg.image.load("game_images/token_black.bmp")
        else:
            self.image = pg.image.load("game_images/token_white.bmp")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = y
        self.rect.centery = x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class TokenBorder:

    def __init__(self, screen, x, y):

        self.screen = screen

        self.image = pg.image.load("game_images/token_border.bmp")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = y
        self.rect.centery = x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class WinMessage:

    def __init__(self, winner):

        pg.font.init()
        font = pg.font.SysFont("arial", 100)
        self.message = font.render(winner + " WINS!", False, (80, 80, 70))


class ButtonText:

    def __init__(self, in_text, font_size):

        pg.font.init()
        font = pg.font.SysFont("arial", font_size)
        self.button_text = font.render(in_text, False, (80, 80, 70))


class Button(pg.Rect):

    def __init__(self, left, top, width, height, screen, color, text=None):

        super().__init__(left, top, width, height)

        self.screen = screen
        self.color = color
        self.text = text

    def add_text(self):

        # TODO Implement

        pass

    def blitme(self):

        pg.draw.rect(self.screen, self.color, self)
