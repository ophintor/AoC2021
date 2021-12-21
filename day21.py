from functools import lru_cache
from itertools import product


def init():
    filename = 'inputs/input21.txt'

    players_position = []
    with open(filename) as f:         
        lines = f.readlines()
        
    for line in lines:
        players_position.append(int(line.strip()[-1]))

    return players_position


def part1():
    players_position = init()
    dice = 0
    dice_rolls = 0
    players_score = [0, 0] 
    max_score = 1000

    while max(players_score) < max_score:      
        for p in range(len(players_position)):
            dice_total = 0
            for _ in range(3):
                dice += 1
                dice_rolls += 1
                dice_total += dice
            dice_total = ((dice_total -1) % 100) + 1

            players_position[p] = ((players_position[p] + dice_total - 1) % 10) + 1
            players_score[p] += players_position[p]
            if players_score[p] >= max_score:
                solution = players_score[p+1%2] * dice_rolls 
                break

    return solution


@lru_cache(maxsize=None)
def new_game(score1, score2, pos1, pos2, player):
    max_score = 21
    all_wins = [0, 0]

    for rolls in product(range(1, 4), repeat=3):
        scores = [score1, score2]
        positions = [pos1, pos2]
        this_roll_wins = [0, 0]

        positions[player] = ((positions[player] + sum(rolls) - 1) % 10) + 1
        scores[player] += positions[player]

        if scores[player] >= max_score:
            all_wins[player] += 1
        else:
            this_roll_wins = new_game(scores[0], scores[1], positions[0], positions[1], ((player+1) %2))

        all_wins[0] += this_roll_wins[0]
        all_wins[1] += this_roll_wins[1]

    return all_wins


def part2():
    positions = init()
    scores = [0, 0]
    wins = new_game(scores[0], scores[1], positions[0], positions[1], player=0)
    return max(wins)


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
