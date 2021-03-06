import unittest
import re
from src.game import game
from src.player import Player

class TestGame(unittest.TestCase):
    def setUp(self):
        self.rock = Player("Dwayne", "rock")
        self.scissors = Player("Edward", "scissors")
        self.paper = Player("Allen", "paper")
        self.cheat = Player("Bruce", "nunchucks")

# test inputs are valid
    def test_input_is_valid(self):
        self.assertEqual("Invalid input: Please enter valid player", game(1, 2))

    def test_one_input_is_invalid(self):
        self.assertEqual("Invalid input: Please enter valid player", game(self.rock, 2))
        self.assertEqual("Invalid input: Please enter valid player", game("string", self.paper))

    def test_player_has_correct_gesture(self):
        self.assertEqual("Invalid gesture: Valid gestures are - rock, paper, scissors.", 
                         game(self.rock, self.cheat))

    def test_not_enough_inputs(self):
        self.assertEqual("not enough players added to the game", game())

    def test_single_player_input_activates_computer(self):
        outcome_as_list = "draw"
        while "draw" in outcome_as_list: 
            outcome_as_list = (game(self.rock)).split()

        self.assertTrue("computer" in outcome_as_list)

# test game win conditions
    def test_game_is_draw(self):
        self.assertEqual("draw: Dwayne and Dwayne both chose rock", game(self.rock, self.rock))

    # Player 1 winner
    def test_rock_beats_scissors_player1_win(self):
        self.assertEqual("Dwayne beat Edward (rock beats scissors)", game(self.rock, self.scissors))
    
    def test_paper_beats_rock_player1_win(self):
        self.assertEqual("Allen beat Dwayne (paper beats rock)", game(self.paper, self.rock))

    def test_scissors_beats_paper_player1_win(self):
        self.assertEqual("Edward beat Allen (scissors beats paper)", game(self.scissors, self.paper))
    
    # Player 2 winner
    def test_rock_beats_scissors_player2_win(self):
        self.assertEqual("Dwayne beat Edward (rock beats scissors)", game(self.scissors, self.rock))

    def test_paper_beats_rock_player2_win(self):
        self.assertEqual("Allen beat Dwayne (paper beats rock)", game(self.rock, self.paper))

    def test_scissors_beats_paper_player2_win(self):
        self.assertEqual("Edward beat Allen (scissors beats paper)", game(self.paper, self.scissors))

    # computer win/lose/draw outcomes 
    def test_computer_opponent_outcomes_randomly_distributed(self):
        outcomes = [0, 0, 0] # player_win, player_lose, draw

        # play 10000 games and check there is an approximately equal distribution of outcomes
        games = 10000        
        for play in range(games):
            result = game(self.paper)
            if "Allen beat computer" in result:
                outcomes[0] += 1
            elif "computer beat Allen" in result:
                outcomes[1] += 1
            else:
                outcomes[2] += 1

        proportions = [outcome / games for outcome in outcomes]
    
        for proportion in proportions:
            self.assertAlmostEqual(0.3, proportion, 1)
        