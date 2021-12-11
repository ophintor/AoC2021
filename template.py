def init():
    filename = 'inputs/inputx.txt'

    # matrix of ints
    matrix = []
    with open(filename) as f:         
        lines = f.readlines()
    for line in lines:
        matrix.append([int(x) for x in list(line.strip())])

    # array of lines
    array_of_ints = []
    with open(filename) as f:         
        lines = f.readlines()
    for line in lines:
        array_of_ints.append([x for x in list(line.strip())])

    # One list of ints
    with open(filename) as f:         
        list_of_ints = [int(x) for x in f.read().split(',')]

    return matrix, array_of_ints, list_of_ints


def part1():
    x = init()
    return 0


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
