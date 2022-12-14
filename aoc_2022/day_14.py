"""day 14 of aoc2022"""

from math import inf
from itertools import product, pairwise


def get_paths(data):
    paths = []

    for d in data:
        path = []
        for s in d.split(' -> '):
            e = s.split(',')
            path.append((int(e[0]), int(e[1])))
        paths.append(path)

    return paths


def get_dimensions(paths):
    x_dim = [inf, 0]
    y_dim = [inf, 0]

    for p in paths:
        for e in p:
            x_dim[0] = min(x_dim[0], e[0])
            x_dim[1] = max(x_dim[1], e[0])
            y_dim[1] = max(y_dim[1], e[1])

    x_dim[0] -= 1
    x_dim[1] += 1
    y_dim[0] = 0
    y_dim[1] += 1
    return (x_dim, y_dim)


def get_grid(paths):
    grid = {}

    for p in paths:
        for e in pairwise(p):
            from_x, to_x = min(e[0][0], e[1][0]), max(e[0][0], e[1][0])
            from_y, to_y = min(e[0][1], e[1][1]), max(e[0][1], e[1][1])
            for x, y in product(
                    range(from_x, to_x + 1),
                    range(from_y, to_y + 1)):
                grid[(x, y)] = '#'

    return grid


def day_14(part, data):
    """solve day 14 for the given part and data."""

    paths = get_paths(data)
    grid = {}
    x_dim, y_dim = get_dimensions(paths)

    x_buffer = 200

    if part == 2:
        y = y_dim[1] + 1
        paths.append([(x_dim[0]-x_buffer, y), (x_dim[1]+x_buffer, y)])
        y_dim[1] += 2
        x_dim[0] -= x_buffer
        x_dim[1] += x_buffer

    grid = get_grid(paths)

    start = (500, 1)
    x, y = start

    while True:
        if (x, y) in grid:

            left = (x-1, y)
            if left not in grid:
                x -= 1
                continue

            right = (x+1, y)
            if right not in grid:
                x += 1
                continue

            pos = (x, y-1)
            if pos in grid:
                break

            grid[pos] = 'o'
            x, y = start
        else:
            y += 1

        if y >= y_dim[1] + 2:
            break

    return sum(1 for k, v in grid.items() if v == "o")
