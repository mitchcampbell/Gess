import sys


class Piece:
    """
    The Piece class represents a 3x3 square of tiles that will be moved
    by a player as a single unit. Pieces will be created by GessGame and
    used to store the position of the player's stones in the piece. The
    positions of the stones will be used by GessGame to determine a
    move's legality and to establish the new position of a player's
    stones after a move is successfully made.
    """

    def __init__(self, board, c, clear=False):
        """
        Initializes a Piece object.

        * board - Board object used to construct piece
        * c - central tile of piece on Board

        _grid
            records position of stones on a GessGame board in 3x3 _grid
            surrounding the given "center" tile, c
        _possible_directions
            represents legal possibilities for the piece's movement direction
            as tuples. E.g. moving up in row number, but down in alphabetic column
            would be (1, -1)
        """

        # If clear parameter is passed, creates empty piece
        if clear:
            self._grid = [[" ", " ", " "],
                          [" ", " ", " "],
                          [" ", " ", " "]]

        # If piece is not intended to be empty, creates piece based on given
        # board center tile position
        else:
            self._grid = [["", "", ""],
                          ["", "", ""],
                          ["", "", ""]]

            for y in (-1, 0, 1):
                for x in (-1, 0, 1):
                    self._grid[y + 1][x + 1] = board.get_state()[c[0] + y][c[1] + x]

        self._possible_directions = self.set_possible_directions()

    def get_grid(self):
        """ Returns _grid """

        return self._grid

    def get_possible_directions(self):
        """ Returns _possible_directions """

        return self._possible_directions

    def set_possible_directions(self):
        """
        Finds all directions in which it is possible for a piece to move.
        Returns as a list of tuples representing movement, i.e. (up/down, left/right)
        """

        possibilities = []

        for y in range(3):
            for x in range(3):
                if self._grid[y][x] != " ":
                    possibilities.append((y - 1, x - 1))

        return possibilities

    def is_empty(self):
        """
        Returns True if Piece is empty. Else, returns False

        Called by Board's legal() function to determine if each space that
        a piece might occupy is empty of stones or not.
        """

        for row in self._grid:
            for col in row:
                if col != " ":
                    return False

        return True

    def place(self, board, c):
        """ Places the piece object on the board """

        top_left = (c[0] - 1, c[1] - 1)

        for y in range(0, 3):
            for x in range(0, 3):
                board.set_tile((top_left[0] + y, top_left[1] + x), self._grid[y][x])


class Board:
    """
    The Board class represents a 20 x 20 GessGame board. A new board will
    be created upon creation of a GessGame, and updated by GessGame as
    players take turns making moves.
    """

    def __init__(self):
        """ A board is created upon the creation of a GessGame object. """

        self._winner = None
        self._state = [
            # a    r    c    d    e    f    g    h    i    j    k    l    m    n    o    p    q    r    s    t
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 1
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],  # 2
            [' ', 'B', 'B', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', ' '],  # 3
            [' ', ' ', 'B', ' ', 'B', ' ', 'B', 'B', 'B', 'B', 'B', 'B', 'B', 'B', ' ', 'B', ' ', 'B', ' ', ' '],  # 4
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 5
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 6
            [' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' ', 'B', ' ', ' '],  # 7
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 8
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 9
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 10
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 11
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 12
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 13
            [' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' ', 'W', ' ', ' '],  # 14
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 15
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 16
            [' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],  # 17
            [' ', 'W', 'W', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', ' '],  # 18
            [' ', ' ', 'W', ' ', 'W', ' ', 'W', 'W', 'W', 'W', 'W', 'W', 'W', 'W', ' ', 'W', ' ', 'W', ' ', ' '],  # 19
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],  # 20
        ]

    def get_state(self):
        """ Returns current board state """

        return self._state

    def get_winner(self):
        """ Returns game winner """

        return self._winner

    def set_winner(self, winner):
        """ Sets game winner """

        self._winner = winner

    def set_tile(self, tile, val):
        """ Sets the given board position (tile) to the given value (val) """

        self._state[tile[0]][tile[1]] = val

    def move(self, start, end, player, opponent):
        """
        Attempts to execute a move provided by GessGame.
        If the move is not legal, returns False.
        If the move is legal, updates game board to reflect move
        and returns True.

        * start - starting position of piece's central tile
        * end - intending ending position of piece's central tile
        * player - current player
        * opponent - opposing player

        Returns True if move is executed, False if not
        """

        # Represents the proposed movement of the piece as (y, x)
        move = (end[0] - start[0], end[1] - start[1])

        temp_state = [list(each) for each in self._state]

        if not self.legal(start, end, move, player, opponent):
            self._state = [list(each) for each in temp_state]
            return False

        if not self.ring_check(opponent):
            self._winner = player

        return True

    def legal(self, start, end, move, player, opponent):
        """
        Checks legality of intended move.
        If move is not legal, returns False. Else, returns True.

        * start - starting position of piece's central tile
        * end - intending ending position of piece's central tile
        * piece - a Piece object, containing the relative position
            of the stones and empty tiles in the piece
        * move - the (x, y) of movement between start and end
        * player - current player
        * opponent - opposing player

        Returns True if move is legal, False if not
        """

        if start == end:
            return False

        # Checks that piece starting and ending position are within the bounds of the game board
        for ord in start + end:
            if ord < 1 or ord > 19:
                return False

        piece = Piece(self, start)

        # Checks that there are none of the opposing teams' stones inside the piece
        for row in piece.get_grid():
            if opponent[0] in row:
                return False

        # Ensures that there is at least one of the player's stones in the piece
        player_found = False

        for row in piece.get_grid():
            if player[0] in row:
                player_found = True

        if not player_found:
            return False

        # Ensures that the move is no greater than 3 spaces if the center tile doesn't contain a stone
        if piece.get_grid()[1][1] == " " and (abs(move[0]) > 3 or abs(move[1]) > 3):
            return False

        # Ensures that the move is either horizontal, vertical or diagonal
        if \
            move[0] != 0 and \
            move[1] != 0 and \
            abs(move[0]) != abs(move[1]):

            return False

        # # Ensures moving in a legal direction
        # Checks diagonal moves
        if move[0] != 0 and move[1] != 0:
            if (move[0] / abs(move[0]), move[1] / abs(move[1])) not in piece.get_possible_directions():
                return False

        # Checks horizontal moves
        if move[1] == 0:
            if (1, 0) not in piece.get_possible_directions() and (-1, 0) not in piece.get_possible_directions():
                return False

        # Checks vertical moves
        if move[0] == 0:
            if (0, 1) not in piece.get_possible_directions() and (0, -1) not in piece.get_possible_directions():
                return False

        # Ensures no stones encountered in path except in destination tile
        blank = Piece(None, None, True)
        blank.place(self, start)

        for coord in self.coordinate_generator(start, end, move):

            temp_piece = Piece(self, coord)
            if not temp_piece.is_empty():
                return False

        # Places piece, checks that player's proposed move does not leave them without a ring
        piece.place(self, end)

        # Clears edges of board
        # Clears rows a and t (indices 0 and 19)
        for row in (0, 19):
            self._state[row] = [" " for col in range(0, 20)]

        # Clears columns 1 and 20 (indices 0 and 19)
        for row in range(1, 19):
            for col in (0, 19):
                self._state[row][col] = " "

        # Do not execute proposed move if it leaves the player with no rings
        if not self.ring_check(player):
            return False

        return True

    def coordinate_generator(self, start, end, move):
        """
        Generates and yields coordinates for piece's movement path

        * start - starting tile
        * end - ending tile
        * move - movement given in format: (delta y, delta x)
        """

        # Generates coordinates for a vertical move
        if move[1] == 0:
            y = start[0]
            while abs(y - end[0]) > 0:
                yield y, start[1]
                if start[0] < end[0]:
                    y += 1
                else:
                    y = y - 1

        # Generates coordinates for a horizontal move
        elif move[0] == 0:
            x = start[1]
            # while abs(x) < abs(end[1]) or abs(x) > abs(end[1]):
            while abs(x - end[1]) > 0:
                yield (start[0], x)
                if start[1] < end[1]:
                    x += 1
                else:
                    x = x - 1

        # Generates coordinates for a diagonal move use slope-intercept formula for a line
        else:
            delta_x = move[1]
            delta_y = move[0]

            # y = mx + r
            # slope = m = rise / run = y2 - y1 / x2 - x1
            m = delta_y / delta_x

            # y = mx + r
            # y - mx = r
            b = start[0] - (m * start[1])

            if start[1] > end[1]:
                x_list = [i for i in range(end[1] + 1, start[1])]
            else:
                x_list = [i for i in range(start[1] + 1, end[1])]

            y_list = [int(m * x + b) for x in x_list]

            for each in range(len(x_list)):
                yield (y_list[each], x_list[each])

    def ring_check(self, player):
        """ Checks if at least one ring for the given player exist on the board """

        for y in range(2, 19):
            for x in range(2, 19):

                if self._state[y][x] == " ":

                    ring_assume = True

                    for y_offset in range(-1, 2):
                        for x_offset in range(-1, 2):
                            if y_offset != 0 or x_offset != 0:
                                if self._state[y + y_offset][x + x_offset] != player[0]:
                                    ring_assume = False

                    if ring_assume:

                        return True

        return False


class GessGame:
    """
    A GessGame object represents a game of Gess. It creates a board object
    and tracks whether the game is still ongoing or which team won. It creates
    piece objects based on the moves attempted by the player. It provides the
    intended moves to the board, and if the board allows the move, updates the
    game status and switches turns between the players as needed.
    """

    def __init__(self):
        """
        A new GessGame creates a new Board object and variables to track the
        current status of the game and which players turn it is, Black always
        starting first.
        """

        self._game_state = "UNFINISHED"
        self._player = "BLACK"
        self._opponent = "WHITE"
        self._board = Board()

    def get_game_state(self):
        """
        Returns one of the following strings describing the status of the game:
            * "BLACK_WON"
            * "WHITE_WON"
            * "UNFINISHED" - means the game has yet to conclude
        """

        return self._game_state

    def get_current_player(self):
        """ Returns color of current player """

        return self._player

    def get_board(self):
        """ Returns the game's board """

        return self._board

    def switch_teams(self):
        """ Switches current player and opponent """

        if self._player == "BLACK":

            self._player = "WHITE"
            self._opponent = "BLACK"

        else:

            self._player = "BLACK"
            self._opponent = "WHITE"

        return None

    def set_winner(self, winner):
        """
        Sets _game_state as won. Returns None

        winner - player to be set as winner in _game_state
        """

        self._game_state = winner + "_WON"

        return None

    def resign_game(self):
        """ Lets a team forfeit the game, calling the game for the opposing team. """

        # Does not allow the game to be resigned if it has already ended
        if self._game_state != "UNFINISHED":
            return False

        self.set_winner(self._opponent)
        self._board.set_winner(self._opponent)

        return None

    def graph(self, alph_num):
        """
        Given a board tile position in alphanumeric format, returns 2d array indices as tuple

        * alpha_num - the letter and number given by the player
        """

        return int(alph_num[1:]) - 1, ord(alph_num[0]) - 97

    def make_move(self, start, end):
        """
        Provides move attempting to be made by player to self._board. If board
        makes move successfully, updates current player

        * start - center tile of piece given by player
        * end - intended ending center tile of piece given by player

        Returns True if move successfully made, returns False if not
        """

        # Translates alphanumeric piece names into 2-d array indices
        start = self.graph(start)
        end = self.graph(end)

        if self._game_state != "UNFINISHED":
            return False

        if not self._board.move(start, end, self._player, self._opponent):
            return False

        # If the board determines that the game has been won, sets winner to
        # current player
        if self._board.get_winner() is not None:
            self.set_winner(self._player)
            return True

        self.switch_teams()

        return True

    def display_board(self):
        """ Displays board on the command line """

        alpha_columns = "abcdefghijklmnopqrst"
        num_rows = "0102030405060708091011121314151617181920"

        print("    ", end='')
        for lett in alpha_columns:
            print(lett, " ", end='')
        print()

        for row in range(len(self.get_board().get_state()) - 1, -1, -1):
            print(num_rows[row * 2 : (row * 2) + 2], " ", end='')
            for col in self.get_board().get_state()[row]:
                print(col, " ", end='')
            print("", num_rows[row * 2: (row * 2) + 2])

        print("    ", end='')
        for lett in alpha_columns:
            print(lett, " ", end='')

        print()


# All lines below this point are for testing only.
def main():

    while True:
        g = GessGame()
        new_game = False

        print("To play, enter starting and ending tiles in format: g7 or g07")

        while not new_game:
            g.display_board()

            print("Player turn:", g.get_current_player())

            start_pos = input("Start tile: ")
            end_pos = input("End tile: ")

            if not g.make_move(start_pos, end_pos):
                print("Illegal move")

            if g.get_game_state() != "UNFINISHED":
                print(g.get_board().get_winner(), "WINS!")

                again = None
                while again not in ["y", "n"]:
                    again = input("Play again? (y/n): ")

                if again in ["y", "Y", "yes", "Yes", "YES"]:
                    new_game = True
                else:
                    sys.exit()


if __name__ == "__main__":
    main()
