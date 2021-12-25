def init():
    filename = 'inputs/input25.txt'

    sea = []
    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        sea.append([x for x in line.strip()])

    return sea


def move_this_fish_east(sea, x, y, next_sea_state):
    len_x = len(sea)
    len_y = len(sea[0])
    moves = 0

    if sea[x%len_x][(y+1)%len_y] == '.':
        next_sea_state[x%len_x][(y+1)%len_y] = '>'
        moves += 1
    else:
        next_sea_state[x][y] = '>'

    return moves


def move_this_fish_south(sea, x, y, next_sea_state):
    len_x = len(sea)
    len_y = len(sea[0])
    moves = 0

    if (sea[(x+1)%len_x][y%len_y] == '.' and sea[(x+1)%len_x][(y-1)%len_y] != '>') or \
        (sea[(x+1)%len_x][y%len_y] == '>' and sea[(x+1)%len_x][(y+1)%len_y] == '.'):
        next_sea_state[(x+1)%len_x][y%len_y] = 'v'
        moves += 1
    else:
        next_sea_state[x][y] = 'v'

    return moves


def move_fishes(sea, next_sea_state, direction):
    moves = 0

    for x in range(len(sea)):
        for y in range(len(sea[0])):
            if direction == 'east' and sea[x][y] == '>':
                moves += move_this_fish_east(sea, x, y, next_sea_state)
            elif direction == 'south' and sea[x][y] == 'v':
                moves += move_this_fish_south(sea, x, y, next_sea_state)
    
    return (moves == 0), next_sea_state


def part1():
    sea = init()
    step = 0
    stalled_east = False
    stalled_south = False

    while not stalled_east or not stalled_south:
        step += 1
        next_sea_state = [[ '.' for x in range(len(sea[0])) ] for y in range(len(sea)) ]
        stalled_east, next_sea_state = move_fishes(sea, next_sea_state,"east")
        stalled_south, next_sea_state = move_fishes(sea, next_sea_state, "south")
        sea = next_sea_state.copy()

    return step


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
