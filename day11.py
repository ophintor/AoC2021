def init():
    filename = 'inputs/input11.txt'
    octopuses = []

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        octopuses.append([int(x) for x in list(line.strip())])

    return octopuses

  
def increase_one(octopuses):
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            octopuses[x][y] += 1


def get_flash_list(octopuses):
    flash_list = {}
    for x in range(len(octopuses)):
        for y in range(len(octopuses[x])):
            if octopuses[x][y] > 9:
                flash_list[(x,y)] = True

    return flash_list


def flash(octopuses):
    size = 10
    flashes = 0

    while True:   
        flash_list = get_flash_list(octopuses)

        if len(flash_list) == 0:
            break
        else:
            flashes += len(flash_list)

            for x,y in flash_list.keys():
                octopuses[x][y] = 0

                if x-1 >= 0:
                    if y-1 >= 0:
                        if octopuses[x-1][y-1] > 0:
                            octopuses[x-1][y-1] += 1
                    if y+1 < size:
                        if octopuses[x-1][y+1] > 0:
                            octopuses[x-1][y+1] += 1

                    if octopuses[x-1][y] > 0:
                        octopuses[x-1][y] += 1

                if x+1 < size:
                    if y-1 >= 0:
                        if octopuses[x+1][y-1] > 0:
                            octopuses[x+1][y-1] += 1
                    if y+1 < size:
                        if octopuses[x+1][y+1] > 0:
                            octopuses[x+1][y+1] += 1
        
                    if octopuses[x+1][y] > 0:
                        octopuses[x+1][y] += 1

                if y-1 >= 0:
                    if octopuses[x][y-1] > 0:
                        octopuses[x][y-1] += 1
    
                if y+1 < size:
                    if octopuses[x][y+1] > 0:
                        octopuses[x][y+1] += 1 
        
    return flashes


def part1():
    times = 100
    flashes = 0
    octopuses = init()
    for t in range(times):
        increase_one(octopuses)
        flashes += flash(octopuses)

    return flashes


def part2():
    counter = 0
    flashes = 0
    octopuses = init()
    while flashes != 100:
        counter += 1
        increase_one(octopuses)
        flashes = flash(octopuses)

    return counter


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
