import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player1 = Player("Allen", "paper")
        self.player2 = Player("CheatinScum", "bazooka")

    def test_player_has_name(self):
        self.assertEqual("Allen", self.player1.name)

    def test_player_has_gesture(self):
        self.assertEqual("paper", self.player1.gesture)

    # def test_player_has_correct_gesture(self):
    #     self.assertEqual("play by the rules, a-hole", self.player2.gesture)
    