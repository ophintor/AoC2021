from binarytree import Node

def init():
    filename = 'inputs/input15.txt'

    matrix = []
    with open(filename) as f:         
        lines = f.readlines()
    for line in lines:
        matrix.append([int(x) for x in list(line.strip())])

    print(matrix)
    return matrix

# def build_tree(matrix, 0, 0):

def part1():
    matrix = init()

    return 0


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
