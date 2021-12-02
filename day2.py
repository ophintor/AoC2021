def part1():
    filename = 'inputs/input2.txt'
    pos = 0
    depth = 0

    with open(filename) as f:
        lines = f.readlines()

    for values in lines:
        instruction = values.split()[0]
        units = int(values.split()[1].strip())
        if instruction == "forward":
            pos += units
        elif instruction == "up":
            depth -= units
        elif instruction == "down":
            depth += units

    print(pos*depth)

def part2():
    filename = 'inputs/input2.txt'
    pos = 0
    depth = 0
    aim = 0

    with open(filename) as f:
        lines = f.readlines()

    for values in lines:
        instruction = values.split()[0]
        units = int(values.split()[1].strip())
        if instruction == "forward":
            pos += units
            depth += (aim * units)
        elif instruction == "up":
            aim -= units
        elif instruction == "down":
            aim += units

    print(pos*depth)

       
if __name__ == '__main__':
    part1()    
    part2()