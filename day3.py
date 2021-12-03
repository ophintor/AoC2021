def init():
    filename = 'inputs/input3.txt'
    bns = []

    with open(filename) as f:
        lines = f.readlines()

    for l in lines:
        bn = l.strip()
        bns.append(bn)
    
    return bns


def calculate_gamma_rate(numbers, size):
    gamma_rate = ""
    epsilon_rate = ""

    for i in range(0,size):
        zeroes = ones = 0 
        for number in numbers:
            if number[i] == "0":
                zeroes += 1
            elif number[i] == "1":
                ones += 1

        if zeroes > ones:
            gamma_rate += "0"
            epsilon_rate += "1"
        else:
            gamma_rate += "1"
            epsilon_rate += "0"

    return gamma_rate, epsilon_rate


def remove_items(numbers, n, pos):
    for index in range(len(numbers)-1,-1,-1):
        if numbers[index][pos] == n:
            del(numbers[index])
    return numbers


def find_rating(numbers, size, criteria):
    for i in range(0, size):
        zeroes = ones = 0 
        for number in numbers:
            if number[i] == "0":
                zeroes += 1
            elif number[i] == "1":
                ones += 1

        if criteria == "ogr":
            if zeroes > ones:
                numbers = remove_items(numbers, "1", i)
            else:
                numbers = remove_items(numbers, "0", i)
        elif criteria == "co2sr":
            if zeroes > ones:
                numbers = remove_items(numbers, "0", i)
            else:
                numbers = remove_items(numbers, "1", i)

        if len(numbers) == 1:
            break

    return int(numbers[0],2)


def part1():
    numbers = init()
    gamma_rate, episilon_rate = calculate_gamma_rate(numbers, len(numbers[0]))
    print(int(gamma_rate, 2) * int(episilon_rate, 2))


def part2():
    numbers = init()
    ogr = find_rating(numbers, len(numbers[0]), "ogr")
    numbers = init()
    co2sr = find_rating(numbers, len(numbers[0]), "co2sr")
    print(ogr*co2sr)


if __name__ == '__main__':
    part1()    
    part2()