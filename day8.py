def init():
    filename = 'inputs/input8.txt'
    entries = []

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        entries.append(line.split(' | '))

    return entries

def part1():
    entries = init()
    total = 0

    for entry in entries:
        output = entry[1].split()
        for o in output:
            if len(o) in (2,3,4,7):
                total += 1
    
    return total


def find_all_candidate_numbers_by_length(signal_patterns, length):
    numbers = []
    for n in signal_patterns:
        n = ''.join(sorted(n))
        if len(n) == length:
            numbers.append(n)
    return numbers
        
def find_number_from_known_one(numbers, current, known):
    for candidate in numbers[current]:
        if set(numbers[known]).issubset(set(candidate)) or set(candidate).issubset(set(numbers[known])):
            numbers[current] = candidate
            break

def decode_numbers(signal_patterns):
    numbers = {}

    # Unique length
    numbers[1] = find_all_candidate_numbers_by_length(signal_patterns, length = 2)[0]
    numbers[7] = find_all_candidate_numbers_by_length(signal_patterns, length = 3)[0]
    numbers[4] = find_all_candidate_numbers_by_length(signal_patterns, length = 4)[0]
    numbers[8] = find_all_candidate_numbers_by_length(signal_patterns, length = 7)[0]

    # Length 6
    numbers[0] = find_all_candidate_numbers_by_length(signal_patterns, length = 6)
    numbers[6] = find_all_candidate_numbers_by_length(signal_patterns, length = 6)
    numbers[9] = find_all_candidate_numbers_by_length(signal_patterns, length = 6)

    # Length 5
    numbers[2] = find_all_candidate_numbers_by_length(signal_patterns, length = 5)
    numbers[3] = find_all_candidate_numbers_by_length(signal_patterns, length = 5)
    numbers[5] = find_all_candidate_numbers_by_length(signal_patterns, length = 5)

    # Derive the rest from others
    find_number_from_known_one(numbers, 3, 1)
    numbers[2].remove(numbers[3])
    numbers[5].remove(numbers[3])

    find_number_from_known_one(numbers, 9, 3)
    numbers[0].remove(numbers[9])
    numbers[6].remove(numbers[9])

    find_number_from_known_one(numbers, 0, 1)
    numbers[6].remove(numbers[0])
    numbers[6] = numbers[6][0]

    find_number_from_known_one(numbers, 5, 9)
    numbers[2].remove(numbers[5])
    numbers[2] = numbers[2][0]

    return numbers


def part2():
    entries = init()
    total = 0

    for entry in entries:
        signal_patterns = entry[0].split()
        output = entry[1].split()
        numbers = decode_numbers(signal_patterns)
        n = ""

        for o in output:
            o = ''.join(sorted(o))
            n += str(list(numbers.keys())[list(numbers.values()).index(o)])

        total += int(n)

    return total


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
