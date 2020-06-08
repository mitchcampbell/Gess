import unittest
from game import GessGame as gg


class GessGameTester(unittest.TestCase):

    def setUp(self):

        self.g0 = gg.GessGame()

        self.g1 = gg.GessGame()
        self.g1.make_move("c8", "c11")
        self.g1.make_move("l14", "r8")
        self.g1.make_move("m6", "j9")

    def test_game_init(self):

        self.assertEqual("UNFINISHED", self.g0.get_game_state())
        self.assertEqual("BLACK", self.g0.get_current_player())

        self.assertIsNone(self.g0._board.winner)

    def test_f07_f11_black(self):

        self.assertEqual(False, self.g0.make_move("f07", "f11"))
