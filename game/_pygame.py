import os
import sys
import pygame as pg
import _state as st
import _rects as r
import _functions as f


def run_game():

    # Initializes PyGame
    pg.init()

    # Creates initial game state
    game = st.GameState()

    # Retrieves game settings
    set = game.settings
    x_off = set.board_x_offset
    y_off = set.board_y_offset

    # Creates viewing window
    screen_change_test = None  # TODO Remove after testing
    screen = pg.display.set_mode((set.screen_width, set.screen_height))
    pg.display.set_caption("Gess")

    #
    background = r.Board(screen, game.settings)

    # Creates background switch buttons
    le = r.Button(775, 50, 50, 30, screen, (200, 200, 200), "Left")
    ri = r.Button(850, 50, 50, 30, screen, (200, 200, 200), "Right")

    # TODO Implement correctly after testing
    # sm = r.Button(775, 90, 50, 30, screen, (200, 200, 200), "Small")
    # la = r.Button(850, 90, 50, 30, screen, (200, 200, 200), "Large")

    # Initializes variables used to track game state
    start_pos = None
    t_border = None
    play_again = False

    while True:

        if screen_change_test is not None:
            screen = pg.display.set_mode((set.screen_width + screen_change_test, set.screen_height + screen_change_test))
            screen_change_test = None

        if play_again:
            game.new_game()
            play_again = False

        # If game is not over, executes main gameplay loop
        if game.game.get_game_state() == "UNFINISHED":

            # Iterates over all input events received since previous loop
            for event in pg.event.get():

                # If window is closed, exits game.
                if event.type == pg.QUIT:
                    sys.exit()

                elif event.type == pg.MOUSEBUTTONDOWN and le.collidepoint(event.pos):
                    game.settings.set_background("left")
                    background = r.Board(screen, game.settings)

                elif event.type == pg.MOUSEBUTTONDOWN and ri.collidepoint(event.pos):
                    game.settings.set_background("right")
                    background = r.Board(screen, game.settings)

                # # TODO Implement correctly after testing
                # elif event.type == pg.MOUSEBUTTONDOWN and sm.collidepoint(event.pos):
                #     screen_change_test = -100
                #
                # # TODO Implement correctly after testing
                # elif event.type == pg.MOUSEBUTTONDOWN and la.collidepoint(event.pos):
                #     screen_change_test = 100

                # Checks for any clicks of the Left Mouse Button (LMB)
                elif \
                        event.type == pg.MOUSEBUTTONDOWN \
                        and event.button == 1 \
                        and 100 < event.pos[0] < 900 \
                        and 100 < event.pos[1] < 900:

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
                        game.game.make_move(
                            tr(start_pos[0] - x_off, start_pos[1] - y_off),
                            tr(click_pos[0] - x_off, click_pos[1] - y_off)
                        )

                        # Resets board for next move
                        start_pos = None
                        t_border = None

        # Draws board and lines to screen
        background.blitme()
        f.draw_lines(screen, x_off, y_off)

        # Draws background image switch buttons to screen
        # TODO Refactor
        le.blitme()
        ri.blitme()
        # sm.blitme()
        # la.blitme()

        # Draws border on selected token, if applicable
        if t_border is not None:
            t_border.blitme()
            f.draw_p_border(screen, t_border)

        # Creates tokens rects and draws them to the screen
        tokens = f.make_tokens(screen, game, x_off, y_off)

        for token in tokens:
            token.blitme()

        # If game is over, draws game over message to screen
        if game.game.get_game_state() != "UNFINISHED":

            # pg.draw.rect(screen, RGB color, Rect((from_left, from_top), (width, height))
            pg.draw.rect(screen, (225, 225, 200), pg.Rect((50, 400), (900, 200)))
            pg.draw.rect(screen, (125, 125, 100), pg.Rect((275, 525), (150, 50)))
            pg.draw.rect(screen, (125, 125, 100), pg.Rect((575, 525), (150, 50)))



            win_message = r.WinMessage(game.game.get_game_state()[:5])
            replay_text = r.ButtonText("Replay")
            exit_text = r.ButtonText("Exit")

            screen.blit(win_message.message, (250, 420))
            screen.blit(replay_text.button_text, (300, 535))
            screen.blit(exit_text.button_text, (625, 535))

            pg.display.update()

            # Awaits player choosing to either play again, or to exit
            while not play_again:

                # Listens for mouse click
                for event in pg.event.get():
                    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                        if 525 < event.pos[1] < 575:
                            if 275 < event.pos[0] < 425:
                                play_again = True

                            elif 575 < event.pos[0] < 725:
                                sys.exit()

        pg.display.update()


run_game()
