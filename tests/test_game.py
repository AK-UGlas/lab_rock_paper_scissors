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

    def test_rock_beats_scissors(self):
        self.assertEqual("rock beats scissors", game(self.player1, self.player2))
    
    def test_paper_beats_rock(self):
        self.assertEqual("paper beats rock", game(self.player1, self.player3))

    def test_scissors_beats_paper(self):
        self.assertEqual("scissors beats paper", game(self.player2, self.player3))
    
    def test_rock_beats_scissors_player2(self):
        self.assertEqual("rock beats scissors", game(self.player2, self.player1))

    def test_paper_beats_rock_player1(self):
        self.assertEqual("paper beats rock", game(self.player3, self.player1))

    def test_scissors_beats_paper_player1(self):
        self.assertEqual("scissors beats paper", game(self.player3, self.player2))

    