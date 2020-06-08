import pygame as pg


class Board:

    def __init__(self, screen):

        self.screen = screen

        # Creates a rect containing the board background image
        self.image = pg.image.load('game_images/boards/1000_wood_teak.bmp')
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
        font = pg.font.SysFont("Comic Sans MS", 100)
        self.message = font.render(winner + " WON!", False, (75, 0, 75))
