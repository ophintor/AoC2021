def init():
    filename = 'inputs/input6.txt'

    with open(filename) as f:         
        fishes = [int(x) for x in f.read().split(',')]

    return fishes


def part1():
    fishes = init()
    days = 80

    for i in range (0, days):
        for fish_index in range(0, len(fishes)):
            if fishes[fish_index] == 0:
                fishes[fish_index] = 6
                fishes.append(8)
            else:
                fishes[fish_index] -= 1

    return len(fishes)
             

def calculate_total_fishes(fish, days, individual_records):
    children = 1
    days = days - fish - 1
    
    for day in range(days, -1, -7):
        if day in individual_records:
            children += individual_records[day]
        else:
            individual_value = calculate_total_fishes(8, day, individual_records)
            individual_records[day] = individual_value
            children += individual_value

    return children
    

def part2():
    fishes = init()
    days = 256
    total = 0
    global_records = {}
    individual_records = {}

    for fish in fishes:
        if fish in global_records:
            total += global_records[fish]
        else:
            fish_global_value = calculate_total_fishes(fish, days, individual_records)
            total += fish_global_value
            global_records[fish] = fish_global_value
                         
    return total


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
