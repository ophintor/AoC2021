from dijkstar import Graph, find_path

def init(size):
    filename = 'inputs/input15.txt'
    matrix = []
    graph = Graph()

    with open(filename) as f:         
        lines = f.readlines()
    
    for i in range(size):
        for line in lines:
            line = [int(x) for x in list(line.strip())]
            bigline = []
            for j in range(size):
                bigline += [ ((x+i+j-1)%9)+1 for x in line ]
            matrix.append(bigline)

    for x in range(len(matrix[0])):
        for y in range(len(matrix)):
            if x == 0 and y == 0:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
            elif x == 0 and y == len(matrix)-1:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
            elif x == len(matrix[0])-1 and y == len(matrix)-1:
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
            elif x == len(matrix[0])-1 and y == 0:
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
            elif x == 0:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
            elif x == len(matrix[0])-1:
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
            elif y == 0:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])
            elif y == len(matrix[0])-1:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
            else:
                graph.add_edge((x,y), (x+1,y), matrix[x+1][y])
                graph.add_edge((x,y), (x,y+1), matrix[x][y+1])
                graph.add_edge((x,y), (x,y-1), matrix[x][y-1])
                graph.add_edge((x,y), (x-1,y), matrix[x-1][y])

    return graph, (len(matrix[0])-1, len(matrix)-1)


def part1():
    graph, end = init(1)
    x = find_path(graph, (0,0), end)
    return x.total_cost


def part2():
    graph, end = init(5)
    x = find_path(graph, (0,0), end)
    return x.total_cost


if __name__ == '__main__':
    print("Solution part 1: %d" % part1())    
    print("Solution part 2: %d" % part2())    
