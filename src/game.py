from src.player import Player

def game(player1, player2):
    # create list of valid gestures
    gestures = ["rock", "paper", "scissors"]

    # check input type
    if type(player1) != Player or type(player2) != Player:
        return "please enter valid player"
    # check gesture valid
    if player1.gesture not in gestures or player2.gesture not in gestures:
        return "play by the rules, a-hole" 

    #if player1.gesture == player2.gesture:
    # if player1 is rock & player2 is scissors
        #return player1 winner
    # if player1 is rock & player2 is paper
        #return player2 winner
    # if player1 is rock & player2 is rock
        #return draw
