def init():
    filename = 'inputs/input17.txt'
    with open(filename) as f:         
        target_area = f.read().split(': ')[1]

    x=target_area.split(', ')[0].split('=')[1]
    y=target_area.split(', ')[1].split('=')[1]
    x1=int(x.split('..')[0])
    x2=int(x.split('..')[1])
    y1=int(y.split('..')[0])
    y2=int(y.split('..')[1])
    
    return x1, x2, y1, y2


def try_velocity(x, y, x1, x2, y1, y2):
    coords = [0,0]
    max_y = 0
    while coords[0] < x2 and coords[1] > y1:
        coords[0] += x
        coords[1] += y
        if coords[1] > max_y: 
            max_y = coords[1]
        if (x1 <= coords[0] <= x2) and (y1 <= coords[1] <= y2):
            return max_y, True
        if x > 0: x -= 1
        elif x < 0: x += 1
        y -= 1
    return 0, False


def part1():
    x1, x2, y1, y2 = init()
    max_y = 0

    for x in range (1, x2+1):
        for y in range(y1, abs(y1)):
            max, hit = try_velocity(x, y, x1, x2, y1, y2)
            if max > max_y: max_y = max
    return max_y


def part2():
    x1, x2, y1, y2 = init()
    on_target = 0

    for x in range (1, x2+1):
        for y in range(y1, abs(y1)):
            max, hit = try_velocity(x, y, x1, x2, y1, y2)
            if hit: on_target += 1
    return on_target


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
