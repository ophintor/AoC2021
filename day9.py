def init():
    filename = 'inputs/input9.txt'
    map = []

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        map.append([int(x) for x in list(line.strip())])

    return map

def is_low_point(map, x, y):
    current = map[x][y]

    if x == 0 and y == 0:
        return map[x+1][y] > current and map[x][y+1] > current
    elif x == 0 and y == len(map[0])-1:
        return map[x+1][y] > current and map[x][y-1] > current
    elif x == len(map)-1 and y == len(map[0])-1:
        return map[x-1][y] > current and map[x][y-1] > current
    elif x == len(map)-1 and y == 0:
        return map[x-1][y] > current and map[x][y+1] > current
    elif x == 0:
        return map[x][y-1] > current and map[x+1][y] > current and map[x][y+1] > current
    elif y == 0:
        return map[x-1][y] > current and map[x+1][y] > current and map[x][y+1] > current
    elif x == len(map)-1:
        return map[x][y-1] > current and map[x-1][y] > current and map[x][y+1] > current
    elif y == len(map[0])-1:
        return map[x-1][y] > current and map[x+1][y] > current and map[x][y-1] > current
    else:
        return map[x-1][y] > current and map[x+1][y] > current and map[x][y-1] > current and map[x][y+1] > current

def part1():
    map = init()
    total = 0
    for x in range(len(map)):
        for y in range(len(map[0])):
            if is_low_point(map, x, y):
                total += 1 + map[x][y]
    
    return total


def calculate_size(map, x, y, tracker):
    tracker[(x,y)] = True
    
    if x > 0 and map[x-1][y] < 9 and (x-1, y) not in tracker:
        calculate_size(map, x-1, y, tracker)
    if x < len(map)-1 and map[x+1][y] < 9 and (x+1, y) not in tracker:
        calculate_size(map, x+1, y, tracker)
    if y > 0 and map[x][y-1] < 9 and (x, y-1) not in tracker:
        calculate_size(map, x, y-1, tracker)
    if y < len(map[0])-1 and map[x][y+1] < 9 and (x, y+1) not in tracker:
        calculate_size(map, x, y+1, tracker)

    return len(tracker)


def part2():
    map = init()
    bassins = []
    for x in range(len(map)):
        for y in range(len(map[0])):
            if is_low_point(map, x, y):
                tracker = {}
                bassin_size = calculate_size(map, x, y, tracker)
                bassins.append(bassin_size)

    bassins.sort(reverse=True)
    return bassins[0] * bassins[1] * bassins[2]


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
