"""day 10 of aoc2022"""


def addx(xs, x, next_x):
    xs.append(next_x)
    xs.append(next_x)
    return next_x + x


grid_w = 40
grid_h = 6


def in_sprite(x, current):
    c_x = current % grid_w
    return abs(c_x - x) <= 1


def print_image(image):
    s = "\n"
    for row in image:
        s += "".join(row) + '\n'
    return s


def day_10(part, data):
    """solve day 10 for the given part and data."""

    next_x = 1
    xs = []

    for d in data:
        if d == 'noop':
            xs.append(next_x)
        else:
            s = d.split()
            value = int(s[1])
            next_x = addx(xs, value, next_x)

    if part == 1:
        to_sum = [20, 60, 100, 140, 180, 220]
        return sum(xs[i-1] * i for i in to_sum)
    else:
        image = [['.'] * grid_w for _ in range(grid_h)]

        for cycle, current in enumerate(xs):
            x = cycle % grid_w
            y = int(cycle / grid_w)
            if in_sprite(x, current):
                image[y][x] = '#'
        return print_image(image)
