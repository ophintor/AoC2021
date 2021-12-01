def part1():
    filename = 'inputs/input1.txt'
    increases = -1
    previous = 0

    with open(filename) as f:
        lines = f.readlines()

    for value in lines:
        current = int(value.strip())
        if current > previous:
            increases += 1
        previous = current

    print(increases)

def part2():
    filename = 'inputs/input1.txt'
    increases = -1
    previous = 0
    values = []

    with open(filename) as f:
        lines = f.readlines()

    for value in lines:
        values.append(int(value.strip()))

    for i in range(0, len(values)-2):
        current = values[i] + values[i+1] + values [i+2]
        if current > previous:
            increases += 1
        previous = current

    print(increases)
       
if __name__ == '__main__':
    part1()    
    part2()