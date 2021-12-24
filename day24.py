def init():
    filename = 'inputs/input24.txt'

    with open(filename) as f:         
        monad = [x.strip() for x in f.readlines()]
        
    return monad

def value_of(var, w, x, y, z):
    if var == 'w':
        return w
    elif var == 'x':
        return x
    elif var == 'y':
        return y
    elif var == 'z':
        return z
    else:
        return int(var)

def process(monad, input):
    variables = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
    input = [int(x) for x in list(str(input))]
    index = 0
    for line in monad:
        instruction = line.split(' ')[0]
        # print(variables['w'], variables['x'], variables['y'], variables['z'])
        # print(line)
        if instruction == 'inp':
            # print("Processing " + str(input[index]))
            a = line.split(' ')[1]
            variables[a] = input[index]
            index += 1
        else:
            a = line.split(' ')[1]
            b = line.split(' ')[2]
            if instruction == 'add':
                if b.lstrip('-').isnumeric():
                    variables[a] = variables[a] + int(b)
                else:
                    variables[a] = variables[a] + variables[b]
            elif instruction == 'mul':
                if b.lstrip('-').isnumeric():
                    variables[a] = variables[a] * int(b)
                else:
                    variables[a] = variables[a] * variables[b]
            elif instruction == 'div':
                if b.lstrip('-').isnumeric():
                    variables[a] = int(variables[a] / int(b))
                else:
                    variables[a] = int(variables[a] / variables[b])
            elif instruction == 'mod':
                if b.lstrip('-').isnumeric():
                    variables[a] = variables[a] % int(b)
                else:
                    variables[a] = variables[a] % variables[b]
            elif instruction == 'eql':
                if b.lstrip('-').isnumeric():
                    variables[a] = 1 if variables[a] == int(b) else 0
                else:
                    variables[a] = 1 if variables[a] == variables[b] else 0
    # print(variables['w'], variables['x'], variables['y'], variables['z'])
    # print("---")
    # print(''.join(str(input)), variables['z'])
    if variables['z'] < 10000:
        print(''.join(str(input)), variables['z'])

    return variables['z']

            

def part1():
    monad = init()
    z = 1000000

    for input in range (99494184689978, 11111111111111, -1):
        if '0' not in str(input) and input % 2730 == 0:
            # print("----------------------------->" + str(input))
            res = process(monad, input)
            if res < z:
                print(input, res)
                z = res
            if z == 0:
                print(input)
                return input


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
