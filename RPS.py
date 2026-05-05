import random

def player(prev_play, opponent_history=[]):
    # First move
    if prev_play == "":
        opponent_history.clear()
        return random.choice(["R", "P", "S"])
    
    # Store opponent move
    opponent_history.append(prev_play)

    # Counter moves
    counter = {"R": "P", "P": "S", "S": "R"}

    # ---- Strategy 1: Pattern detection ----
    if len(opponent_history) > 3:
        pattern = "".join(opponent_history[-3:])
        patterns = {}

        for i in range(len(opponent_history) - 3):
            seq = "".join(opponent_history[i:i+3])
            next_move = opponent_history[i+3]
            
            if seq not in patterns:
                patterns[seq] = {"R": 0, "P": 0, "S": 0}
            
            patterns[seq][next_move] += 1

        if pattern in patterns:
            prediction = max(patterns[pattern], key=patterns[pattern].get)
            return counter[prediction]

    # ---- Strategy 2: Frequency analysis ----
    if len(opponent_history) > 10:
        most_common = max(set(opponent_history), key=opponent_history.count)
        return counter[most_common]

    # ---- Strategy 3: Random fallback ----
    return random.choice(["R", "P", "S"])

