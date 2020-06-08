import pygame as pg
import _rects as r


def make_tokens(screen, game, x_off, y_off):
    """
    Creates a list of Token rects based on current board state, for drawing to the board.
    """
    # Draws tokens on board
    board = game.game.get_board().get_state()

    # For each tile on board, if the tile is not blank, creates Token and adds to list
    tokens = []

    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] != " ":
                tokens.append(
                    r.Token(
                        screen,
                        board[row][col],
                        (row * 40) + 20 + x_off,
                        (col * 40) + 20 + y_off
                    )
                )

    return tokens


def draw_lines(screen, x_offset, y_offset):
    """
    Draws lines bordering each tile on the game board.
    """

    for x in range(0, 800 + 1, 40):
        pg.draw.line(screen, (0, 0, 0), (x + x_offset, 0 + y_offset), (x + x_offset, 800 + y_offset), 3)

    for y in range(0, 800 + 1, 40):
        pg.draw.line(screen, (0, 0, 0), (0 + x_offset, y + y_offset), (800 + x_offset, y + y_offset), 3)


def draw_p_border(screen, t_border):
    """
    Draws a border around the selected piece
    """

    corners = []
    for x in (-60, 60):
        for y in (-60, 60):
            corners.append((x, y))

    sides = [(0, 1), (1, 3), (3, 2), (2, 0)]

    for s in sides:
        pg.draw.line(
            screen,
            (255, 0, 0),
            (t_border.rect.centerx + corners[s[0]][0], t_border.rect.centery + corners[s[0]][1]),
            (t_border.rect.centerx + corners[s[1]][0], t_border.rect.centery + corners[s[1]][1]),
            5)

def tile_translate(x, y):
    """
    Translates the given (y, x) coordinate pair of a user's mouse click on
    an 800x800 game board to the format of a tile position on a Gess game board

    Example
    :param y: 350
    :param x: 415
    :return:
    """

    alphas = "abcdefghijklmnopqrst"
    nums = "0102030405060708091011121314151617181920"

    return alphas[x // 40] + nums[(y // 40) * 2: (y // 40) * 2 + 2]