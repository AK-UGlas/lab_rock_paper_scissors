import unittest
from src.game import game
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Josh", "rock")
        self.player2 = Player("Spencer", "scissors")
        self.player = Player("Allen", "paper")

    def test_input_is_valid(self):
        self.assertEqual("please enter valid player", game(1, 2))

    