import pygame as pg


class Settings:

    def __init__(self):
        self.screen_width = 800
        self.screen_height = 800
        self.bg_color = (60, 60, 60)
        self.bg_image = pg.image.load("_gessgame_images/board.bmp")


# class Game_State:
#
#     def __init__(self):
#         # TODO Move game state parameters here
