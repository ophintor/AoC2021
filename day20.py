import numpy as np

def init():
    filename = 'inputs/input20.txt'

    with open(filename) as f:
        lines = f.readlines()

    algorithm = list(lines[0])

    input = []
    for line in lines[2:]:
        input.append([x for x in list(line.strip())])

    return algorithm, input


def pretty(m):
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                print('.', end='')
            else:
                print('#', end='')
        print("")
    print("")


def get_binary(input):
    binary = []
    for i in input:
        if i == '.':
            binary.append(0)
        else:
            binary.append(1)
    return binary


def expand_image(input, padding):
    expanded_image = []
    for i in range(padding):
        expanded_image.append([0] * ((2 * padding) + len(input)))
    for i in range(len(input)):
        binary_input = get_binary(input[i])
        expanded_image.append([0] * padding + binary_input + [0] * padding)
    for i in range(padding):
        expanded_image.append([0] * ((2 * padding) + len(input)))
    return expanded_image


def transform(input, output, alg):
    for i in range(1, len(input)-1):
        for j in range(1, len(input[0])-1):
            pixels = str(input[i-1][j-1]) + str(input[i-1][j]) + str(input[i-1][j+1]) + str(input[i][j-1]) + \
                     str(input[i][j]) + str(input[i][j+1]) + str(input[i+1][j-1]) + str(input[i+1][j]) + \
                     str(input[i+1][j+1])
            
            pixels_index = int(pixels, 2)

            if alg[pixels_index] == '.':
                output[i][j] = 0
            else:
                output[i][j] = 1

    return output


def part1():
    alg, input = init()
    iterations = 2
    padding = iterations * 2
    input = expand_image(input, padding)
    output = [[0 for _ in range(len(input))] for _ in range(len(input))]

    for i in range(iterations):
        input = transform(input, output, alg)
        output = np.array(output)

    # crop the crap
    output = output[iterations:len(output)-iterations, iterations:len(output[0])-iterations]

    return np.count_nonzero(output == 1)


def part2():
    alg, input = init()
    iterations = 50
    padding = iterations * 2
    input = expand_image(input, padding)
    output = [[0 for _ in range(len(input))] for _ in range(len(input))]

    for i in range(iterations):
        input = transform(input, output, alg)
        output = np.array(output)

    # crop the crap
    output = output[iterations:len(output)-iterations, iterations:len(output[0])-iterations]

    return np.count_nonzero(output == 1)


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())
    print("Solution part 2: %d" % part2())
