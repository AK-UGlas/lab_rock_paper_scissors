import unittest
from src.game import game
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Josh", "rock")
        self.player2 = Player("Spencer", "scissors")
        self.player3 = Player("Allen", "paper")
        self.player4 = Player("Cheat", "nunchucks")
        self.player5 = Player("Colin", "rock")

    def test_input_is_valid(self):
        self.assertEqual("please enter valid player", game(1, 2))

    def test_input_1_is_invalid(self):
        self.assertEqual("please enter valid player", game(self.player1, 2))

    def test_player_has_correct_gesture(self):
        self.assertEqual("play by the rules, a-hole", game(self.player1, self.player4))

    def test_game_is_draw(self):
        self.assertEqual("draw", game(self.player1, self.player5))
    