from RPS import player

# simulate opponent moves
moves = ["R", "P", "S", "R", "P", "S"]

for move in moves:
    print("Opponent:", move)
    print("Player:", player(move))
