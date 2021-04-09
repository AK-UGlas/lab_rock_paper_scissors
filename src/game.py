from src.player import Player
from random import choice

# A simple Rock, Paper, Scissors game:

def game(*args):
    """  --- Rock Paper Scissors --- 
    Can be played with 2 player characters or a single player and computer with a randomly assigned gesture 
    """

    # generate list of valid gestures
    gestures = ["rock", "paper", "scissors"]

    # check inputs are valid 
    if len(args) == 0:
        return "not enough players added to the game"
    elif len(args) < 3:
        for player in args:
            if type(player) != Player:
                return "Invalid input: Please enter valid player"
    else: 
        return "too many players: Only 2 players can be added to the game"

    #assign players
    player1, player2 = args[0], None

    if len(args) == 1:
        player2 = Player("computer", choice(gestures))
    else:
        player2 = args[1]

    # check gesture valid
    if player1.gesture not in gestures or player2.gesture not in gestures:
        error_msg = "Invalid gesture: Valid gestures are - "
        punctuation = ""
        for gesture in range(len(gestures)):
            if gesture == len(gestures) - 1:
                punctuation = "."
            else:
                punctuation = ", "
            error_msg += gestures[gesture] + punctuation
        
        return error_msg

    # if gestures are equal its a draw
    if player1.gesture == player2.gesture:
        return "draw"
    
    # check all winning player1 scenarios...
    if ( (player1.gesture == "rock" and player2.gesture == "scissors") or   
         (player1.gesture == "scissors" and player2.gesture == "paper") or
         (player1.gesture == "paper" and player2.gesture == "rock") ):
            winner = player1
            loser = player2
    else:
        # if we get here, player2 must have won
        winner = player2
        loser = player1

    return f"{winner.name} beat {loser.name} ({winner.gesture} beats {loser.gesture})"
       