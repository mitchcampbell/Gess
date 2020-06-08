import GessGame as GG
import pygame as pg


class GameState:

    def __init__(self):
        self.game = GG.GessGame()
        self.settings = Settings()


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 1000
        self.board_x_offset = 100
        self.board_y_offset = 100
        self.bg_image = pg.image.load("game_images/board.bmp")

