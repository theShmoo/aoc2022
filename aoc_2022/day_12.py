"""day 12 of aoc2022"""


from itertools import product


def print_grid(grid, edges):
    s = ""
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            if (x, y) in edges:
                s += '#'
            else:
                s += chr(c)
        s += '\n'
    print(s)


def find_start_and_end(grid):
    height = len(grid)
    width = len(grid[0])

    for x, y in product(range(width), range(height)):
        current = grid[y][x]
        if current == ord('S'):
            start = (x, y)
            grid[y][x] = ord('a')
        elif current == ord('E'):
            end = (x, y)
            grid[y][x] = ord('z')

    return (start, end)


def get_edges(grid):
    height = len(grid)
    width = len(grid[0])
    edges = {}

    for x, y in product(range(width), range(height)):
        current = grid[y][x]
        neighbours = {}
        if y > 0 and current - grid[y-1][x] < 2:
            neighbours[(x, y-1)] = 1
        if y < height-1 and current - grid[y+1][x] < 2:
            neighbours[(x, y+1)] = 1
        if x > 0 and current - grid[y][x-1] < 2:
            neighbours[(x-1, y)] = 1
        if x < width - 1 and current - grid[y][x+1] < 2:
            neighbours[(x+1, y)] = 1
        edges[(x, y)] = neighbours

    return edges


def get_nodes(grid):
    height = len(grid)
    width = len(grid[0])
    return [(x, y) for x, y in product(range(width), range(height))]


def dijkstra(grid, start, nodes, edges):

    unvisited = {node: None for node in nodes}
    visited = {}
    current = start
    current_dist = 0
    unvisited[current] = current_dist

    while (True):
        for neighbour, distance in edges[current].items():
            if neighbour not in unvisited:
                continue
            new_dist = current_dist + distance
            if unvisited[neighbour] is None or unvisited[neighbour] > new_dist:
                unvisited[neighbour] = new_dist
        visited[current] = current_dist
        del unvisited[current]
        candidates = [node for node in unvisited.items() if node[1]]
        if not candidates:
            break
        current, current_dist = sorted(candidates, key=lambda x: x[1])[0]

    return visited


def day_12(part, data):
    """solve day 12 for the given part and data."""

    grid = [[ord(c) for c in d] for d in data]
    start, end = find_start_and_end(grid)

    nodes = get_nodes(grid)
    edges = get_edges(grid)

    distances = dijkstra(grid, end, nodes, edges)

    if part == 1:
        return distances[start]
    else:
        return min(distances[e] for e in edges.keys()
                   if grid[e[1]][e[0]] == ord('a') and e in distances)
