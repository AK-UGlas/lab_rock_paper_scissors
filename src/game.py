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

    # if gestures are equal its a draw
    if player1.gesture == player2.gesture:
        return "draw"
    
    # if player1 is rock & player2 is scissors
        #return player1 winner
    if player1.gesture == "rock":
        if player2.gesture == "scissors":
            return "rock beats scissors"
        return "paper beats rock"
    # if player1 is rock & player2 is paper
        #return player2 winner
    elif player1.gesture == "scissors":
        if player2.gesture == "paper":
            return "scissors beats paper"
        return "rock beats scissors"

    # play
    elif player1.gesture == "paper":
        if player2.gesture == "rock":
            return "paper beats rock"
        return "scissors beats paper"

    
