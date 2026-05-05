import random

def quincy(prev_play, counter=[0]):
    counter[0] += 1
    choices = ["R", "R", "P", "P", "S"]
    return choices[counter[0] % len(choices)]

def play(player1, player2, num_games, verbose=False):
    p1_prev = ""
    p2_prev = ""

    p1_score = 0
    p2_score = 0

    for _ in range(num_games):
        p1 = player1(p2_prev)
        p2 = player2(p1_prev)

        p1_prev = p1
        p2_prev = p2

        if p1 == p2:
            continue
        elif (p1 == "R" and p2 == "S") or \
             (p1 == "P" and p2 == "R") or \
             (p1 == "S" and p2 == "P"):
            p1_score += 1
        else:
            p2_score += 1

        if verbose:
            print(f"P1: {p1}  P2: {p2}")

    print("Player 1 win rate:", p1_score / num_games * 100)
