"""day 08 of aoc2022"""

from itertools import product
import copy


def print_grid(grid):
    for x in grid:
        print(x)


def day_08(part, data):
    """solve day 08 for the given part and data."""

    height = len(data)

    grid = [list(data[y]) for y in range(height)]
    print_grid(grid)

    width = len(grid[0])

    candidates = [[0] * height for w in range(width)]

    # left
    left = copy.deepcopy(grid)
    left_score = copy.deepcopy(candidates)

    for x, y in product(range(width), range(height)):
        if x == 0:
            candidates[x][y] = 1
        else:
            if left[x][y] > left[x-1][y]:
                candidates[x][y] = 1
                left_score[x][y] = left_score[x-1][y] + 1
            else:
                left[x][y] = left[x-1][y]
                left_score[x][y] = 0

    right = copy.deepcopy(grid)
    for x, y in product(reversed(range(width)), range(height)):
        if x == width - 1:
            candidates[x][y] = 1
        else:
            if right[x][y] > right[x+1][y]:
                candidates[x][y] = 1
            else:
                right[x][y] = right[x+1][y]

    top = copy.deepcopy(grid)
    for x, y in product(range(width), range(height)):
        if y == 0:
            candidates[x][y] = 1
        else:
            if top[x][y] > top[x][y-1]:
                candidates[x][y] = 1
            else:
                top[x][y] = top[x][y-1]

    bottom = copy.deepcopy(grid)
    for x, y in product(range(width), reversed(range(height))):
        if y == height - 1:
            candidates[x][y] = 1
        else:
            if bottom[x][y] > bottom[x][y+1]:
                candidates[x][y] = 1
            else:
                bottom[x][y] = bottom[x][y+1]

    if part == 1:
        return sum(candidates[x][y] for x, y in
                   product(range(width),
                           range(height)))
