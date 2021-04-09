import unittest
from src.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.paper = Player("Allen", "paper")
        self.bazooka = Player("CheatinScum", "bazooka")

    def test_player_has_name(self):
        self.assertEqual("Allen", self.paper.name)

    def test_player_has_gesture(self):
        self.assertEqual("bazooka", self.bazooka.gesture)

    
    