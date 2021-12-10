def init():
    filename = "inputs/input10.txt"
    code = []

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        code.append([x for x in list(line.strip())])

    return code


def get_opposite(c):
    if   c == "(": return ")"
    elif c == "[": return "]"
    elif c == "{": return "}"
    elif c == "<": return ">" 


def process_line(line, tracker, index):
    if index < len(line):
        if line[index] in ("(", "[", "{", "<"):
            tracker.append(line[index])
            process_line(line, tracker, index+1)
        elif line[index] == get_opposite(tracker[-1]):
            tracker.pop()
            process_line(line, tracker, index+1)
        else:
            tracker.append(line[index])


def part1():
    code = init()
    total = 0
    for line in code:
        tracker = []
        process_line(line, tracker, index=0)
        if   tracker[-1] == ")" : total += 3
        elif tracker[-1] == "]" : total += 57
        elif tracker[-1] == "}" : total += 1197
        elif tracker[-1] == ">" : total += 25137

    return total


def part2():
    code = init()
    scores = []
    for line in code:
        tracker = []
        process_line(line, tracker, index=0)
        tracker.reverse()
        if tracker[0] in ("(","[","{","<"):
            total = 0
            for chunk in tracker:
                total *= 5
                if   chunk == "(" : total += 1 
                elif chunk == "[" : total += 2
                elif chunk == "{" : total += 3 
                elif chunk == "<" : total += 4 
            scores.append(total)

    scores.sort()
    return scores[int(len(scores)/2)]


if __name__ == "__main__":
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
