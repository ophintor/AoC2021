def init():
    filename = 'inputs/input7.txt'

    with open(filename) as f:         
        positions = [int(x) for x in f.read().split(',')]

    return positions

def calculate_fuel_flat(positions, position):
    total_fuel = 0
    for p in positions:
        total_fuel += abs(position - p)
    return total_fuel

def calculate_fuel_incremental(positions, position):
    total_fuel = 0
    for p in positions:
        total_fuel += sum(range(1, abs(position - p)+1))
    return total_fuel

def part1():
    positions = init()
    fuel_cost = {}
    for position in range(min(positions), max(positions) + 1):
        fuel_cost[position] = calculate_fuel_flat(positions, position)
    
    return min(fuel_cost.values())
             
def part2():
    positions = init()
    fuel_cost = {}
    for position in range(min(positions), max(positions) + 1):
        fuel_cost[position] = calculate_fuel_incremental(positions, position)
    
    return min(fuel_cost.values())


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
