"""day 04 of aoc2022"""


def get_range(elve):
    r = elve.split('-')
    return int(r[0]), int(r[1])


def day_04(part, data):
    """solve day 04 for the given part and data."""

    contains = 0

    for line in data:

        elves = line.split(',')
        rs = [get_range(e) for e in elves]

        if rs[0][0] > rs[1][0] or (
                rs[0][0] == rs[1][0] and rs[0][1] < rs[1][1]):
            rs[1], rs[0] = rs[0], rs[1]

        l1, r1 = rs[0]
        l2, r2 = rs[1]

        if (part == 1 and r1 >= r2) or (part == 2 and r1 >= l2):
            contains = contains + 1

    return contains
