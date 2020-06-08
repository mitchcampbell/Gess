import sys
import pygame as pg
import GessGame as GG
import _state as st
import _rects as r
import _functions as f


def run_game():

    # Initializes PyGame
    pg.init()

    # Retrieves game settings
    settings = st.Settings()

    # Creates viewing window
    screen = pg.display.set_mode((settings.screen_width, settings.screen_height))
    pg.display.set_caption("Gess")
    x_off = settings.board_x_offset
    y_off = settings.board_y_offset

    #
    background = r.Board(screen)

    game = GG.GessGame()

    # Initializes variables used to track game state
    won = False
    winner = None
    start_pos = None
    t_border = None

    # Main gameplay loop
    while True:

        if not won:

            # Iterates over all input events received since previous loop
            for event in pg.event.get():

                # If window is closed, exits game.
                if event.type == pg.QUIT:
                    sys.exit()

                # Checks for any clicks of the Left Mouse Button (LMB)
                elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:

                    # If the starting position has not already been selected,
                    # sets mouse click to starting move position and creates
                    # a border around the selected token
                    if start_pos is None:

                        start_pos = event.pos
                        t_border = r.TokenBorder(
                            screen,
                            (((start_pos[1] - x_off) // 40) * 40) + 20 + x_off,
                            (((start_pos[0] - x_off) // 40) * 40) + 20 + x_off
                        )

                    # If the starting position had already been selected, sets
                    # position of LMB click to end position
                    else:

                        click_pos = event.pos

                        tr = f.tile_translate
                        # Translates x, y positions of mouse click to game board tile inputs
                        # and attempts move
                        game.make_move(
                            tr(start_pos[0] - x_off, start_pos[1] - y_off),
                            tr(click_pos[0] - x_off, click_pos[1] - y_off)
                        )

                        # Resets board for next move
                        start_pos = None
                        t_border = None

        # Draws board and lines to screen
        background.blitme()
        f.draw_lines(screen, x_off, y_off)

        # Draws border on selected token, if applicable
        if t_border is not None:
            t_border.blitme()
            f.draw_p_border(screen, t_border)

        # Creates tokens rects and draws them to the screen
        tokens = f.make_tokens(screen, game, x_off, y_off)

        for token in tokens:
            token.blitme()

        # TODO
        if game.get_game_state() != "UNFINISHED":
            win_message = r.WinMessage(game.get_game_state()[:5])
            screen.blit(win_message.message, (50, 340))

            # for event in pg.event.get():
            #     if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            #         # TODO Check whether mouse clicked on "Play Again"

        pg.display.update()


run_game()
