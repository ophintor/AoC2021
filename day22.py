from collections import defaultdict
from functools import lru_cache
from typing import overload

def init():
    filename = 'inputs/input22.txt'

    instructions = []
    with open(filename) as f:         
        lines = f.readlines()

    for line in lines:
        instructions.append(line.strip())

    return instructions


def part1():
    instructions = init()
    cubes = defaultdict(int)
    total = 0
    for ins in instructions:
        command = 1 if ins.split(' ')[0] == 'on' else 0
        x1, x2 = [int(a) for a in ins.split('x=')[1].split(',')[0].split('..')]
        y1, y2 = [int(a) for a in ins.split('y=')[1].split(',')[0].split('..')]
        z1, z2 = [int(a) for a in ins.split('z=')[1].split(',')[0].split('..')]
        for x in range(max(-50,x1), min(51,x2+1)):
            for y in range(max(-50,y1), min(51,y2+1)):
                for z in range(max(-50,z1), min(51,z2+1)):
                    cubes[(x,y,z)] = command
    total += sum(value == 1 for value in cubes.values())
    return total


# def turn_on(cubes, x1, x2, y1, y2, z1, z2):
#     overlap = 0
#     cube_size = (x2-x1+1) * (y2-y1+1) * (z2-z1+1)
#     for cube in cubes:
#         x_over = len(list(set(range(x1,x2+1)) & set(range(cube[0], cube[1]+1))))
#         y_over = len(list(set(range(y1,y2+1)) & set(range(cube[2], cube[3]+1))))
#         z_over = len(list(set(range(z1,z2+1)) & set(range(cube[4], cube[5]+1))))
#         overlap += abs(x_over * y_over * z_over)
#     cubes.append((x1,x2,y1,y2,z1,z2))
#     print("size : %d" % cube_size)
#     print("overlap : %d" % overlap)
#     print("adding : %d" % (cube_size - overlap))

#     return cube_size - overlap


# def is_already_turned_off(cube, turned_off_list):
#     is_off = False
#     for cube_off in turned_off_list:
#         is_off = cube_off[0] <= cube[0] <= cube_off[1] and cube_off[0] <= cube[1] <= cube_off[1] and \
#                 cube_off[2] <= cube[2] <= cube_off[3] and cube_off[2] <= cube[3] <= cube_off[3] and \
#                 cube_off[4] <= cube[4] <= cube_off[5] and cube_off[4] <= cube[5] <= cube_off[5]
#     return is_off


# def remove_minicubes_that_are_off(mini_cubes, x1, x2, y1, y2, z1, z2, already_turned_off_cubes):
#     remove_list = []
#     total_overlap = 0
#     for cube in mini_cubes:
#         if  x1 <= cube[0] <= x2 and x1 <= cube[1] <= x2 and \
#             y1 <= cube[2] <= y2 and y1 <= cube[3] <= y2 and \
#             z1 <= cube[4] <= z2 and z1 <= cube[5] <= z2:        
#             x_over = len(list(set(range(x1,x2+1)) & set(range(cube[0], cube[1]+1))))
#             y_over = len(list(set(range(y1,y2+1)) & set(range(cube[2], cube[3]+1))))
#             z_over = len(list(set(range(z1,z2+1)) & set(range(cube[4], cube[5]+1))))
#             overlap = abs(x_over * y_over * z_over)
#             if overlap > 0 and not is_already_turned_off(cube, already_turned_off_cubes):
#                 # print("Turning off: %s" % str(cube))
#                 already_turned_off_cubes.append(cube)
#                 total_overlap += overlap
#                 remove_list.append(cube)
#     for cube_to_remove in remove_list:
#         mini_cubes.remove(cube_to_remove)
    
#     return total_overlap


# def turn_off(cubes, x1, x2, y1, y2, z1, z2):
#     off_list = []
#     already_turned_off_cubes = []
#     total_overlap = 0

#     # First update cubes list with all mini-cubes based on overlaps
#     for cube_index in range(len(cubes)):
#         cube = cubes[cube_index]
#         mini_cubes = [cube]
#         new_mini_cubes = []
#         cubes_to_remove = []

#         for c in mini_cubes:
#             if c[0] < x1 < c[1] and c[0] <= x2 <= c[1]:
#                 new_mini_cubes.append((c[0],x1-1, c[2], c[3], c[4], c[5]))
#                 new_mini_cubes.append((x1, x2, c[2], c[3], c[4], c[5]))
#                 new_mini_cubes.append((x2+1, c[1], c[2], c[3], c[4], c[5]))
#             elif c[0] < x1 < c[1]:
#                 new_mini_cubes.append((c[0],x1-1, c[2], c[3], c[4], c[5]))
#                 new_mini_cubes.append((x1, c[1], c[2], c[3], c[4], c[5]))
#             elif c[0] < x2 < c[1]:
#                 new_mini_cubes.append((c[0], x2, c[2], c[3], c[4], c[5]))
#                 new_mini_cubes.append((x2+1, c[1], c[2], c[3], c[4], c[5]))

#             if new_mini_cubes:
#                 cubes_to_remove.append(c)
#                 # total_overlap += remove_minicubes_that_are_off(new_mini_cubes, x1, x2, y1, y2, z1, z2, already_turned_off_cubes)

#         mini_cubes.extend(new_mini_cubes)
#         # print(mini_cubes)
#         for ctr in cubes_to_remove:
#             mini_cubes.remove(ctr)

#         new_mini_cubes = []
#         cubes_to_remove = []
#         for c in mini_cubes:
#             if c[2] < y1 < c[3] and c[2] <= y2 <= c[3]:
#                 new_mini_cubes.append((c[0],c[1], c[2], y1-1, c[4], c[5]))
#                 new_mini_cubes.append((c[0],c[1], y1, y2, c[4], c[5]))
#                 new_mini_cubes.append((c[0],c[1], y2+1, c[3], c[4], c[5]))
#             elif c[2] < y1 < c[3]:
#                 new_mini_cubes.append((c[0],c[1], c[2], y1-1, c[4], c[5]))
#                 new_mini_cubes.append((c[0],c[1], y1, c[3], c[4], c[5]))
#             elif c[2] < y2 < c[3]:
#                 new_mini_cubes.append((c[0],c[1], c[2], y2, c[4], c[5]))
#                 new_mini_cubes.append((c[0],c[1], y2+1, c[3], c[4], c[5]))

#             if new_mini_cubes:
#                 # total_overlap += remove_minicubes_that_are_off(new_mini_cubes, x1, x2, y1, y2, z1, z2, already_turned_off_cubes)
#                 cubes_to_remove.append(c)

#         mini_cubes.extend(new_mini_cubes)
#         # print(mini_cubes)
#         for ctr in cubes_to_remove:
#             mini_cubes.remove(ctr)

#         new_mini_cubes = []
#         cubes_to_remove = []
#         for c in mini_cubes:
#             if c[4] < z1 < c[5] and c[4] <= z2 <= c[5]:
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z1-1))
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], z1, z2))
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], z2+1, c[5]))
#             elif c[4] < z1 < c[5]:
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z1-1))
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], z1, c[5]))
#             elif c[4] < z2 < c[5]:
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z2))
#                 new_mini_cubes.append((c[0],c[1], c[2], c[3], z2+1, c[5]))

#             if new_mini_cubes:
#                 # total_overlap += remove_minicubes_that_are_off(new_mini_cubes, x1, x2, y1, y2, z1, z2, already_turned_off_cubes)
#                 cubes_to_remove.append(c)

#         total_overlap += remove_minicubes_that_are_off(new_mini_cubes, x1, x2, y1, y2, z1, z2, already_turned_off_cubes)
#         mini_cubes.extend(new_mini_cubes)
#         # print(mini_cubes)
#         for ctr in cubes_to_remove:
#             mini_cubes.remove(ctr)

#         # Update cubes
#         if len(mini_cubes) > 1:
#             cubes.extend(mini_cubes)
#             off_list.append(cube)
                             
#     for off in off_list:
#         cubes.remove(off)

#     print("Turning off: %d" % total_overlap)

#     return total_overlap


# def part2():
#     instructions = init()
#     cubes = []
#     total = 0

#     for ins in instructions:
#         print('')
#         print(ins)
#         command = 1 if ins.split(' ')[0] == 'on' else 0
#         x1, x2 = [int(a) for a in ins.split('x=')[1].split(',')[0].split('..')]
#         y1, y2 = [int(a) for a in ins.split('y=')[1].split(',')[0].split('..')]
#         z1, z2 = [int(a) for a in ins.split('z=')[1].split(',')[0].split('..')]
        
#         if command == 1:
#             total += turn_on(cubes, x1, x2, y1, y2, z1, z2)
#         elif command==0:
#             total -= turn_off(cubes, x1, x2, y1, y2, z1, z2)

#         # print(cubes)
#         # print("TOTAL %d" % total)

#     return total



def get_size(cube):
    return (cube[1]-cube[0]+1) * (cube[3]-cube[2]+1) * (cube[5]-cube[4]+1)


def calculate_axis_intersection(axis):
    if max(axis[0], axis[2]) <= min(axis[1], axis[3]):
        return(max(axis[0], axis[2]), min(axis[1], axis[3]))
    else:
        return None, None


def calculate_intersections(c1, c2):
    xs = [c1[0], c1[1], c2[0], c2[1]]
    ys = [c1[2], c1[3], c2[2], c2[3]]
    zs = [c1[4], c1[5], c2[4], c2[5]]
    x1, x2 = calculate_axis_intersection(xs)
    y1, y2 = calculate_axis_intersection(ys)
    z1, z2 = calculate_axis_intersection(zs)
    inters = set()
    if not None in (x1, x2, y1, y2, z1, z2):
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                for z in range(z1, z2+1):
                    inters.add((x,y,z))

    return inters

def get_intersections(cube, cubes, intersections, command):
    overlap = 0
    set_size = len(intersections)
    for c in cubes:
        inters = calculate_intersections(c, cube)
        if command == 1:
            intersections = intersections | inters
            overlap += len(inters)
        else:
            intersections = intersections - inters

    if command == 0:      
        overlap += (set_size - len(intersections))

    return overlap, intersections

def divide_and_shut_down(cubes, cube_off):
    off_list = []
    x1, x2, y1, y2, z1, z2 = cube_off[0], cube_off[1], cube_off[2], cube_off[3], cube_off[4], cube_off[5]

    # First update cubes list with all mini-cubes based on overlaps
    for cube_index in range(len(cubes)):
        cube = cubes[cube_index]
        mini_cubes = [cube]
        new_mini_cubes = []
        cubes_to_remove = []

        for c in mini_cubes:
            if c[0] < x1 < c[1] and c[0] <= x2 <= c[1]:
                new_mini_cubes.append((c[0],x1-1, c[2], c[3], c[4], c[5]))
                new_mini_cubes.append((x1, x2, c[2], c[3], c[4], c[5]))
                new_mini_cubes.append((x2+1, c[1], c[2], c[3], c[4], c[5]))
            elif c[0] < x1 < c[1]:
                new_mini_cubes.append((c[0],x1-1, c[2], c[3], c[4], c[5]))
                new_mini_cubes.append((x1, c[1], c[2], c[3], c[4], c[5]))
            elif c[0] < x2 < c[1]:
                new_mini_cubes.append((c[0], x2, c[2], c[3], c[4], c[5]))
                new_mini_cubes.append((x2+1, c[1], c[2], c[3], c[4], c[5]))

            if new_mini_cubes:
                cubes_to_remove.append(c)

        mini_cubes.extend(new_mini_cubes)
        for ctr in cubes_to_remove:
            mini_cubes.remove(ctr)

        new_mini_cubes = []
        cubes_to_remove = []
        for c in mini_cubes:
            if c[2] < y1 < c[3] and c[2] <= y2 <= c[3]:
                new_mini_cubes.append((c[0],c[1], c[2], y1-1, c[4], c[5]))
                new_mini_cubes.append((c[0],c[1], y1, y2, c[4], c[5]))
                new_mini_cubes.append((c[0],c[1], y2+1, c[3], c[4], c[5]))
            elif c[2] < y1 < c[3]:
                new_mini_cubes.append((c[0],c[1], c[2], y1-1, c[4], c[5]))
                new_mini_cubes.append((c[0],c[1], y1, c[3], c[4], c[5]))
            elif c[2] < y2 < c[3]:
                new_mini_cubes.append((c[0],c[1], c[2], y2, c[4], c[5]))
                new_mini_cubes.append((c[0],c[1], y2+1, c[3], c[4], c[5]))

            if new_mini_cubes:
                cubes_to_remove.append(c)

        mini_cubes.extend(new_mini_cubes)
        for ctr in cubes_to_remove:
            mini_cubes.remove(ctr)

        new_mini_cubes = []
        cubes_to_remove = []
        for c in mini_cubes:
            if c[4] < z1 < c[5] and c[4] <= z2 <= c[5]:
                new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z1-1))
                new_mini_cubes.append((c[0],c[1], c[2], c[3], z1, z2))
                new_mini_cubes.append((c[0],c[1], c[2], c[3], z2+1, c[5]))
            elif c[4] < z1 < c[5]:
                new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z1-1))
                new_mini_cubes.append((c[0],c[1], c[2], c[3], z1, c[5]))
            elif c[4] < z2 < c[5]:
                new_mini_cubes.append((c[0],c[1], c[2], c[3], c[4], z2))
                new_mini_cubes.append((c[0],c[1], c[2], c[3], z2+1, c[5]))

            if new_mini_cubes:
                cubes_to_remove.append(c)

        mini_cubes.extend(new_mini_cubes)
        for ctr in cubes_to_remove:
            mini_cubes.remove(ctr)

        # Update cubes with minicubes
        if len(mini_cubes) > 1:
            remove_minicubes_that_are_off(mini_cubes, x1, x2, y1, y2, z1, z2)
            cubes.extend(mini_cubes)
            off_list.append(cube)

    # Remove big cubes
    for off in off_list:
        cubes.remove(off)

def remove_minicubes_that_are_off(mini_cubes, x1, x2, y1, y2, z1, z2):
    remove_list = []
    for cube in mini_cubes:
        if  x1 <= cube[0] <= x2 and x1 <= cube[1] <= x2 and \
            y1 <= cube[2] <= y2 and y1 <= cube[3] <= y2 and \
            z1 <= cube[4] <= z2 and z1 <= cube[5] <= z2:        
            x_over = len(list(set(range(x1,x2+1)) & set(range(cube[0], cube[1]+1))))
            y_over = len(list(set(range(y1,y2+1)) & set(range(cube[2], cube[3]+1))))
            z_over = len(list(set(range(z1,z2+1)) & set(range(cube[4], cube[5]+1))))
            overlap = abs(x_over * y_over * z_over)
            if overlap > 0:
                remove_list.append(cube)

    for cube_to_remove in remove_list:
        mini_cubes.remove(cube_to_remove)

def turn_on(cubes, intersections, cube):
    size = get_size(cube)
    overlap, intersections = get_intersections(cube, cubes, intersections, 1)
    # print(size, overlap)
    if size > overlap:
        # print("overlap: %d" % overlap)
        cubes.append(cube)
        print("tuning on: %s " % (size - overlap))
        print("--")
        return (size - overlap), intersections
    else:
        return 0, intersections

def intersection_exists(i, cubes):
    for cube in cubes:
        if cube[0] <= i[0] <= cube[1] and cube[2] <= i[1] <= cube[3] and cube[4] <= i[2] <= cube[5]:
            return True
    return False

def update_intersections(cubes, intersections):
    remove_list = []
    for i in intersections:
        if not intersection_exists(i, cubes):
            remove_list.append(i)

    for item in remove_list:
        intersections.remove(item)

def turn_off(cubes, intersections, cube):
    overlap, intersections = get_intersections(cube, cubes, intersections, 0)
    size = 0
    for c in cubes:
        int_points = calculate_intersections(c, cube)
        if int_points:
            size += get_size((min(int_points)[0], max(int_points)[0], min(int_points)[1], max(int_points)[1], min(int_points)[2], max(int_points)[2]))
    
    if size > 0:
        divide_and_shut_down(cubes, cube)

    update_intersections(cubes, intersections)
    # print("o %d" % overlap)
    size -= overlap
    intersections = intersections - int_points
    print("tuning off: %s " % (size))
    print("--")
    return size, intersections

def part2():
    instructions = init()
    cubes = []
    intersections = set()
    total = 0

    for ins in instructions:
        command = 1 if ins.split(' ')[0] == 'on' else 0
        x1, x2 = [int(a) for a in ins.split('x=')[1].split(',')[0].split('..')]
        y1, y2 = [int(a) for a in ins.split('y=')[1].split(',')[0].split('..')]
        z1, z2 = [int(a) for a in ins.split('z=')[1].split(',')[0].split('..')]
        cube = (x1, x2, y1, y2, z1, z2)

        if command == 1:
            count_on, intersections = turn_on(cubes, intersections, cube)
            total += count_on
        elif command == 0:
            count_off, intersections = turn_off(cubes, intersections, cube)
            total -= count_off

    return total


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
