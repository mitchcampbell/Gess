import pygame as pg


class Board:

    def __init__(self, screen):

        self.screen = screen

        self.image = pg.image.load('_gessgame_images/board.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

    def blitme(self):

        self.screen.blit(self.image, self.rect)


class Token:

    def __init__(self, screen, team, x, y):

        self.screen = screen

        self.team = team
        if self.team == "B":
            self.image = pg.image.load("_gessgame_images/token_black.bmp")
        else:
            self.image = pg.image.load("_gessgame_images/token_white.bmp")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = y
        self.rect.centery = x

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class TokenBorder:

    def __init__(self, screen, x, y):

        self.screen = screen

        self.image = pg.image.load("_gessgame_images/token_border.bmp")

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = y
        self.rect.centery = x

    def blitme(self):
        self.screen.blit(self.image, self.rect)