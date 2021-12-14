import collections

def init():
    filename = 'inputs/input14.txt'
    rules = {}

    with open(filename) as f:    
        all = f.read().split('\n\n')       

    for line in all[1].split('\n'):
        rules[line.split(' -> ')[0]] = line.split(' -> ')[1]

    return all[0], rules


def calculate_difference_slow(polymer, rules, steps):
    for _ in range(steps):
        new_polymer = polymer[0]
        for i in range(0, len(polymer)-1):
            pair = polymer[i:i+2]
            new_polymer += rules[pair] + polymer[i+1]
        polymer = new_polymer
    stats = dict(collections.Counter(polymer).most_common())
    return max(stats.values()) - min(stats.values())


def calculate_difference_fast(polymer, rules, steps):
    stats = dict(collections.Counter(polymer).most_common())
    pairs = {}

    # Initialise dict of pairs
    for i in range(0, len(polymer)-1):
        pair = polymer[i:i+2]
        if pair not in pairs:
            pairs[pair] = 1
        else:
            pairs[pair] += 1

    # Calculate the good stuff
    for _ in range(steps):
        new_pairs = {}
        for pair in list(pairs.keys()):
            element = rules[pair]
            pairs_amount = pairs[pair]

            # Update elements        
            if element in stats:
                stats[element] += pairs_amount
            else: 
                stats[element] = pairs_amount

            # Update dictionary of pairs in a brand new dictionary
            if pair[0] + element in new_pairs.keys():
                new_pairs[pair[0] + element] += pairs_amount
            else:
                new_pairs[pair[0] + element] = pairs_amount

            if element + pair[1] in new_pairs.keys():
                new_pairs[element + pair[1]] += pairs_amount
            else:
                new_pairs[element + pair[1]] = pairs_amount

        # Update dictionary of pairs
        pairs = new_pairs

    return max(stats.values()) - min(stats.values())


def part1(steps):
    return calculate_difference_slow(polymer, rules, steps)


def part2(steps):
    return calculate_difference_fast(polymer, rules, steps)


if __name__ == '__main__':
    polymer, rules = init()
    print("Solution part 1: %d" % part1(10))    
    print("Solution part 2: %d" % part2(40))    
