import re

def init():
    filename = 'inputs/input23.txt'
    rooms = {'A': [], 'B': [], 'C': [], 'D': []}

    with open(filename) as f:         
        lines = f.readlines()

    for line in lines[2:4]:
        amphipods = re.findall("[A-D]+", line)      
        rooms['A'].append(amphipods[0])
        rooms['B'].append(amphipods[1])
        rooms['C'].append(amphipods[2])
        rooms['D'].append(amphipods[3])

    return rooms



def part1():

    print("Doing it manually is simpler...")

    #############
    #...........#
    ###D#D#A#A###
      #C#C#B#B#
      #########

    energy = 0

    #############
    #AA.......B.#
    ###D#D# # ###
      #C#C#B# #
      #########

    energy += 8 + 7 + 30

    #############
    #AA.......B.#
    ### # # #D###
      #C#C#B#D#
      #########

    energy += 8000 + 7000

    #############
    #AA.....B.B.#
    ### # # #D###
      #C#C# #D#
      #########

    energy += 30

    #############
    #AA.....B.B.#
    ### # #C#D###
      # # #C#D#
      #########

    energy += 600 + 700

    #############
    #...........#
    ###A#B#C#D###
      #A#B#C#D#
      #########

    energy += 50 + 60 + 3 + 3

    return energy

# 16464 no
# 16491 no


def part2():
    x = init()
    return 0


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
