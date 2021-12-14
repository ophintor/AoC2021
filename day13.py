def init():
    filename = 'inputs/input13.txt'
    points = []
    instructions = []

    with open(filename) as f:    
        all = f.read().split('\n\n')       

    for pos in all[0].split('\n'):
        points.append(tuple(map(int, pos.split(','))))

    for line in all[1].split('\n'):
        coord = line.split()[2].strip()
        instructions.append(coord)

    return points, instructions

def pretty(m):
    for x in range(len(m)):
        for y in range(len(m[x])):
            if m[x][y] == 1:
                print('#', end=' ')
            else:
                print (' ', end=' ')
        print('')
    print('')
    

def fold(matrix, point):
    pos = int(point.split('=')[1])
    if point.split('=')[0] == 'y':
        folded_matrix = []
        for i in range(pos):
            folded_matrix.append(matrix[i])
            for j in range(len(matrix[i])):
                if matrix[2*pos-i][j] == 1:
                    folded_matrix[i][j] = 1
    elif point.split('=')[0] == 'x':
        folded_matrix = []
        for i in range(len(matrix)):
            folded_matrix.append(matrix[i][0:pos])
            for j in range(pos):
                if matrix[i][2*pos-j] == 1:
                    folded_matrix[i][j] = 1               

    return folded_matrix

def part1():
    points, instructions = init()
    h = max([pos[0] for pos in points])
    l = max([pos[1] for pos in points])
    matrix = [[0 for x in range(h+1)] for y in range(l+1)]
    for point in points:
        matrix[point[1]][point[0]] = 1

    folded_matrix = fold(matrix, instructions[0])
    
    total = 0
    for i in range(len(folded_matrix)):
        for j in range(len(folded_matrix[i])):
            if folded_matrix[i][j] == 1:
                total += 1

    return total

def part2():
    points, instructions = init()
    h = max([pos[0] for pos in points])
    l = max([pos[1] for pos in points])
    matrix = [[0 for x in range(h+1)] for y in range(l+1)]
    for point in points:
        matrix[point[1]][point[0]] = 1

    for i in instructions:
        matrix = fold(matrix, i)
    
    pretty(matrix)


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2:")
    part2()    
