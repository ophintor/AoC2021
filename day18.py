import math

def init():
    filename = "inputs/input18.txt"

    sf_numbers = []
    with open(filename) as f:         
        lines = f.readlines()
    for line in lines:
        sf_numbers.append(list(line.strip()))

    return sf_numbers


def get_depth(sf_number):
    depth = 0
    max_depth = 0
    for i in range(len(sf_number)):
        if sf_number[i] == "[":
            depth += 1
            if depth > max_depth:
                max_depth = depth
        elif sf_number[i] == "]":
            depth -= 1
    return max_depth


def get_index_of_next_number_on_the_left(sf_number, i):
    distance = 0
    while i >= 0:
        if sf_number[i] == "[":
            distance += 1
            i -= 1
        elif sf_number[i] in ("]", ","):
            i -= 1
        else:
            return i, distance
    return None, distance


def get_index_of_next_number_on_the_right(sf_number, i):
    distance = 0
    while i < len(sf_number):
        if sf_number[i] == "]":
            distance += 1
            i += 1
        elif sf_number[i] in ("[", ","):
            i += 1
        else:
            return i, distance
    return None, distance


def explode(sf_number, max_depth):
    depth = 0
    i = 0
    # do left side
    while i < len(sf_number):
        if sf_number[i] == "[":
            depth += 1
            if depth == max_depth:
                i += 1
                # i on first internal number
                nl, distance = get_index_of_next_number_on_the_left(sf_number, i-1)
                if nl and distance == 1:
                    sf_number[nl] = str(int(sf_number[nl]) + int(sf_number[i]))
                    del(sf_number[nl+2:nl+5])
                    i -= 1
                elif nl:
                    sf_number[nl] = str(int(sf_number[nl]) + int(sf_number[i]))
                    sf_number[i] = "0"
                    del(sf_number[i-1])
                    i += 1
                else:
                    sf_number[i] = "0"
                    del(sf_number[i-1])
                    i += 1
                # i on second internal number
                nr, distance = get_index_of_next_number_on_the_right(sf_number, i+1)
                if nr and distance == 1:
                    sf_number[nr] = str(int(sf_number[nr]) + int(sf_number[i]))
                    del(sf_number[i:i+3])
                elif nr:
                    sf_number[nr] = str(int(sf_number[nr]) + int(sf_number[i]))
                    sf_number[i] = "0"
                    del(sf_number[i+1])
                    i += 1
                else:
                    sf_number[i] = "0"
                    del(sf_number[i+1])
                    i += 1
                break
        elif sf_number[i] == "]":
            depth -= 1
        i += 1


def split(sf_number):
    i = 0
    while i < len(sf_number) - 1:
        if sf_number[i].isnumeric() and int(sf_number[i]) > 9:
            number = int(sf_number[i])
            del(sf_number[i])
            sf_number.insert(i, "]")
            sf_number.insert(i, str(int(math.ceil(number/2))))
            sf_number.insert(i, ",")
            sf_number.insert(i, str(int(math.floor(number/2))))
            sf_number.insert(i, "[")

            break
        i += 1


def big_numbers_exist(sf_number):
    for i in range(len(sf_number)):
        if sf_number[i].isnumeric() and int(sf_number[i]) > 9:
            return True
    return False


def reduce(sf_number):
    depth = get_depth(sf_number)
    while depth > 4 or big_numbers_exist(sf_number):
        while depth > 4:
            explode(sf_number, depth)
            depth = get_depth(sf_number)
        split(sf_number)
        depth = get_depth(sf_number)


def build_sum_sf(sfn1, sfn2):
    if sfn1 == []:
        return sfn2
    else:
        sfn1.insert(0, "[")
        sfn1.insert(len(sfn1), ",")
        sfn1.extend(sfn2)
        sfn1.insert(len(sfn1), "]")
        return (sfn1)


def get_magnitude(sf_number):
    while get_depth(sf_number) > 0:
        i = 0 
        while i < len(sf_number):
            if sf_number[i] == '[' and sf_number[i+1].isnumeric() and sf_number[i+2] == ',' and sf_number[i+3].isnumeric() and sf_number[i+4] == ']':
                sf_number[i] = str(int(sf_number[i+1])*3 + int(sf_number[i+3])*2)
                del(sf_number[i+1:i+5])
            i += 1
    return int(sf_number[0])


def part1():
    sf_numbers = init()
    sum_sf = []
    for i in range(len(sf_numbers)):
        sum_sf = build_sum_sf(sum_sf, sf_numbers[i])
        reduce(sum_sf)
    mag = get_magnitude(sum_sf)
    return mag


def part2():
    sf_numbers = init()
    max_mag = 0
    for i in range(len(sf_numbers)):
        for j in range(len(sf_numbers)):
            if i != j and get_depth(list(sf_numbers[i])) > 3 and get_depth(list(sf_numbers[j])) > 3:
                sum_sf = build_sum_sf(list(sf_numbers[i]), list(sf_numbers[j]))
                reduce(sum_sf)
                mag = get_magnitude(sum_sf)
                if mag > max_mag:
                    max_mag = mag
    return max_mag
    

if __name__ == "__main__":
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
