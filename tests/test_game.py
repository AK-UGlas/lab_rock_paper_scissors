import unittest
from src.game import game
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Josh", "rock")
        self.player2 = Player("Spencer", "scissors")
        