"""day 05 of aoc2022"""

import re


def get_stacks(input):
    size = len(input[-1])
    num_stacks = int((size+2) / 4)

    stacks = [[] for j in range(num_stacks)]

    for line in input[:-1]:
        for i, e in enumerate(line):
            if e.isupper():
                stacks[int((i+1) / 4)].append(e)

    for s in stacks:
        s.reverse()

    return stacks


def get_moves(input):
    return [[int(f) for f in re.findall(r'\d+', i)] for i in input]


def day_05(part, data):
    """solve day 05 for the given part and data."""

    separator = data.index("")

    stacks = get_stacks(data[:separator])
    moves = get_moves(data[(separator+1):])

    for m in moves:
        num_moves = m[0]
        source = stacks[m[1]-1]
        target = stacks[m[2]-1]

        to_move = source[-num_moves:]
        del source[-num_moves:]

        if part == 1:
            to_move.reverse()

        target.extend(to_move)

    result = str()
    for s in stacks:
        result += s.pop()

    return result
