from enum import Enum

class Player(Enum):
    P1 = 1
    P2 = 2

def tenis_game(points):

    game =["Love", "15", "30", "40"]
    p1_points = 0
    p2_points = 0


    for player in points:

        if player == Player.P1:
            P1_points += 1
        elif player == Player.P2:
            P2_points += 1

            if P1_points >= 3 and P2_points >= 3:


tenis_game([Player.P1, Player.P1, Player.P2, Player.P2, 
Player.P1, Player.P2, Player.P1, Player.P1])

