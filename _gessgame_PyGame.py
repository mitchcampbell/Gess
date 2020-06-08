import sys
import pygame as pg
import _gessgame_settings
import _gessgame_rects as r
import _gessgame_funcs as f
import GessGame as GG


def run_game():

    # Initializes PyGame
    pg.init()

    # Retrieves game settings
    set = _gessgame_settings.Settings()

    # Creates viewing window
    screen = pg.display.set_mode((set.screen_width, set.screen_height))
    pg.display.set_caption("Gess")

    #
    bg_image = r.Board(screen)

    game = GG.GessGame()
    board = game.get_board().get_state()

    # Initializes variables used to track game state
    won = False
    winner = None
    start_pos = None
    border = None

    # Main gameplay loop
    while True:

        if not won:

            # Iterates over all input events received since previous loop
            for event in pg.event.get():

                # If window is closed, exits game.
                if event.type == pg.QUIT:
                    sys.exit()

                #
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                    if start_pos is None:

                        start_pos = event.pos
                        border = r.TokenBorder(
                            screen,
                            ((start_pos[1] // 40) * 40) + 20,
                            ((start_pos[0] // 40) * 40) + 20
                        )

                    #
                    else:

                        click_pos = event.pos

                        alphas = "abcdefghijklmnopqrst"
                        nums = "0102030405060708091011121314151617181920"

                        # TODO remove below line after done testing
                        # print(start_pos[0] // 40) + (nums[start_pos[1] // 40) * 2 : (start_pos[1] // 40) * 2 + 2

                        if not game.make_move(
                            alphas[start_pos[0] // 40] + nums[(start_pos[1] // 40) * 2: (start_pos[1] // 40) * 2 + 2],
                            alphas[click_pos[0] // 40] + nums[(click_pos[1] // 40) * 2: (click_pos[1] // 40) * 2 + 2],
                        ):
                            if game.get_game_state() != "UNFINISHED":
                                won = True
                                winner = game.get_game_state()[:5]

                        start_pos = None
                        border = None

        # Draws board to screen
        bg_image.blitme()

        # Draws lines on board
        for x in range(40, 800, 40):
            pg.draw.line(screen, (0, 0, 0), (x, 0), (x, 800), 3)

        for y in range(40, 800, 40):
            pg.draw.line(screen, (0, 0, 0), (0, y), (800, y), 3)

        # Draws border on selected token, if applicable
        if border is not None:
            border.blitme()

            corners = []
            for x in (-60, 60):
                for y in (-60, 60):
                    corners.append((x, y))

            sides = [(0, 1), (1, 3), (3, 2), (2, 0)]

            for s in sides:
                pg.draw.line(
                    screen,
                    (255, 0, 0),
                    (border.rect.centerx + corners[s[0]][0], border.rect.centery + corners[s[0]][1]),
                    (border.rect.centerx + corners[s[1]][0], border.rect.centery + corners[s[1]][1]),
                    5)

        board = game.get_board().get_state()

        tokens = []
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] != " ":
                    tokens.append(
                        r.Token(screen, board[row][col], (row * 40) + 20, (col * 40) + 20)
                    )

        for token in tokens:
            token.blitme()

        if won:
            pg.font.init()
            font = pg.font.SysFont("Comic Sans MS", 100)
            win_message = font.render(winner + " WON!", False, (75, 0, 75))
            screen.blit(win_message, (50, 340))

        pg.display.update()


run_game()
