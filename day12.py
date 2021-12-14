def init():
    filename = 'inputs/input12.txt'

    directions = {}
    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        a = line.strip().split('-')[0]
        b = line.strip().split('-')[1]
        
        if a == "start" or b == 'end':
            if a in directions:
                directions[a].append(b)
            else:
                directions[a] = [b]
        elif a == "end" or b == 'start':
            if b in directions:
                directions[b].append(a)
            else:
                directions[b] = [a]
        else:
            if a in directions:
                directions[a].append(b)
            else:
                directions[a] = [b]

            if b in directions:
                directions[b].append(a)
            else:
                directions[b] = [a]

    return directions


def get_distinct_paths(directions, cave, tracker):
    counter = 0
    if cave == 'end':
        return 1
    elif cave.isupper() or (cave.islower() and cave not in tracker):
        for next in directions[cave]:
            tracker.append(cave)
            counter += get_distinct_paths(directions, next, tracker)
            tracker.pop()

    return counter


def is_this_cave_allowed(here, tracker):
    if here == 'start' and len(tracker) > 0:
        return False
    else:
        minor_caves_visited = [x for x in tracker if x.islower()]
        if here in minor_caves_visited and len(set(minor_caves_visited)) < len(minor_caves_visited):
            return False
    return True
            

def get_distinct_paths_with_one_repetition(directions, cave, tracker):
    counter = 0
    if cave == 'end':
        return 1
    elif cave.isupper() or (cave.islower() and is_this_cave_allowed(cave, tracker)):
        for next in directions[cave]:
            tracker.append(cave)
            counter += get_distinct_paths_with_one_repetition(directions, next, tracker)
            tracker.pop()

    return counter

def part1():
    directions = init()
    tracker = []
    counter = get_distinct_paths(directions, 'start', tracker)
    return counter

def part2():
    directions = init()
    tracker = []
    counter = get_distinct_paths_with_one_repetition(directions, 'start', tracker)
    return counter

if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
