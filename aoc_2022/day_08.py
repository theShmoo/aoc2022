"""day 08 of aoc2022"""

from itertools import product


def count_visible(height, arr):
    count = 0
    for i in arr:
        count += 1
        if i >= height:
            break
    return count


def is_maximum(height, arr):
    return max(arr) < height


def day_08(part, data):
    """solve day 08 for the given part and data."""

    height = len(data)

    grid = [[int(x) for x in data[y]] for y in range(height)]
    grid_t = [list(x) for x in zip(*grid)]

    width = len(grid[0])

    if part == 1:
        fun = is_maximum
        score = width * 2 + (height - 2) * 2
    else:
        fun = count_visible
        score = 0

    for x, y in product(range(1, width-1), range(1, height-1)):
        h = grid[x][y]

        left = fun(h, reversed(grid[x][:y]))
        right = fun(h, grid[x][y + 1:])
        top = fun(h, reversed(grid_t[y][:x]))
        bottom = fun(h, grid_t[y][x + 1:])

        if part == 1:
            if left or right or top or bottom:
                score += 1
        else:
            new_score = left * right * top * bottom
            score = max(score, new_score)

    return score
