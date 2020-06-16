import os
import GessGame as GG
import pygame as pg
import _rects as r

class GameState:

    def __init__(self):
        self.game = GG.GessGame()
        self.settings = Settings()

    def new_game(self):
        self.game = GG.GessGame()


class Settings:

    def __init__(self):
        self.screen_width = 1000
        self.screen_height = 1000
        self.board_x_offset = 100
        self.board_y_offset = 100
        self.bg_image_num = 0
        self.bg_image = r"1000_wood_burnt.jpg"

    def set_background(self, direction):

        if direction == "left":
            self.bg_image_num = self.bg_image_num - 1
        elif direction == "right":
            self.bg_image_num += 1

        options = len(os.listdir(r"game_images/boards"))

        if self.bg_image_num < 0:
            self.bg_image_num = options - 1
        elif self.bg_image_num >= options:
            self.bg_image_num = 0

        self.bg_image = os.listdir(r"game_images/boards")[self.bg_image_num]