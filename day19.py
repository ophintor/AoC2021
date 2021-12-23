import numpy as np

def init():
    filename = 'inputs/input19.txt'
    reports = {}

    with open(filename) as f:         
        lines = f.readlines()

    for i in range(len(lines)):
        if lines[i].startswith("---"):
            key = int(lines[i].split(' ')[2])
            reports[key] = []
        elif lines[i] != '\n':
            reports[key].append(tuple([int(x) for x in lines[i].strip().split(',')]))
        i += 1

    return reports


def pretty(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            print(m[i][j], end =' ')
        print('')


def get_map(scanner):
    xs = [elem[0] for elem in scanner]
    ys = [elem[1] for elem in scanner]
    zs = [elem[2] for elem in scanner]
    min_x, max_x = min(xs), max(xs)
    min_y, max_y = min(ys), max(ys)
    min_z, max_z = min(zs), max(zs)
    map = np.zeros(((max_x - min_x + 1), (max_y - min_y + 1), (max_z - min_z + 1)))
    for pos in scanner:
        map[pos[0]-min_x][pos[1]-min_y][pos[2]-min_z] = 1

    return(map)


def check_all_rotations_matches(m1, m2):
    counter = 0
    for nr in range(4):
        for axis1 in range(3):
            for axis2 in range(3):
                if axis1 != axis2:
                    # counter += 1
                    # print(counter)
                    m1 = np.rot90(m1, nr, (axis1,axis2))
                    # if (m1.shape == m2.shape):   
                    m = np.where((m1 == m2), m1, 0)
                    matches = np.count_nonzero(m == 1)
                    if matches >= 12:
                        print("Matches: " + str(matches))




def part1():
    reports = init()
    # print(reports)
    maps = []
    for scanner in reports.values():
        map = get_map(scanner)
        maps.append(map)

    for i in range(len(maps)-1):
        for j in range(len(maps)-1):
            if i!= j:
                # print("checking all rotations... " + str(i))
                check_all_rotations_matches(maps[i], maps[j])

    return 0


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
