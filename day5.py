import sys

def init():
    filename = 'inputs/input5.txt'
    lines_list = []

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        start, end = line.split(' -> ')
        x1, y1 = start.strip().split(',')
        x2, y2 = end.strip().split(',')
        lines_list.append([(int(x1),int(y1)),(int(x2),int(y2))])

    return lines_list


def part1():
    lines = init()
    positions = {}
    for line in lines:
        if line[0][0] == line[1][0]:
            for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                positions[line[0][0], y] = positions[line[0][0], y] + 1 if (line[0][0], y) in positions else 1
        elif line[0][1] == line[1][1]:
            for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                positions[x, line[0][1]] = positions[x, line[0][1]] + 1 if (x, line[0][1]) in positions else 1
    
    return str(len([x for x,n in positions.items() if n>1]))

def part2():
    lines = init()
    positions = {}
    for line in lines:
        if line[0][0] == line[1][0]:
            for y in range(min(line[0][1], line[1][1]), max(line[0][1], line[1][1]) + 1):
                positions[line[0][0], y] = positions[line[0][0], y] + 1 if (line[0][0], y) in positions else 1
        elif line[0][1] == line[1][1]:
            for x in range(min(line[0][0], line[1][0]), max(line[0][0], line[1][0]) + 1):
                positions[x, line[0][1]] = positions[x, line[0][1]] + 1 if (x, line[0][1]) in positions else 1
        else:
            step_x = 1 if line[0][0] < line[1][0] else -1
            step_y = 1 if line[0][1] < line[1][1] else -1
            y = line[0][1]
            for x in range(line[0][0], line[1][0] + step_x, step_x):
                positions[x, y] = positions[x, y] + 1 if (x, y) in positions else 1
                y += step_y
    
    return str(len([x for x,n in positions.items() if n>1]))

if __name__ == '__main__':
    print("Solution part 1: " + part1())    
    print("Solution part 2: " + part2())    
