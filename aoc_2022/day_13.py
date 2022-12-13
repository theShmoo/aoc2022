"""day 13 of aoc2022"""

from itertools import groupby
from functools import cmp_to_key


def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def compare_lists(lhs, rhs):

    l_lhs, l_rhs = len(lhs), len(rhs)

    length = min([l_lhs, l_rhs])

    for i in range(length):
        c = compare(lhs[i], rhs[i])
        if c != 0:
            return c

    return l_lhs - l_rhs


def compare(lhs, rhs):
    t_lhs, t_rhs = type(lhs), type(rhs)

    if t_lhs != t_rhs:
        if t_lhs is not list:
            return compare_lists([lhs], rhs)
        else:
            return compare_lists(lhs, [rhs])

    if t_lhs == int and t_rhs == int:
        return lhs - rhs

    return compare_lists(lhs, rhs)


def day_13(part, data):
    """solve day 13 for the given part and data."""

    packets = []
    for k, g in groupby(data, lambda s: not s):
        if not k:
            packets.extend([eval(a) for a in g])

    if part == 1:
        invalid = []
        pairs = chunks(packets, 2)
        for i, p in enumerate(pairs):
            print(p)
            if compare(p[0], p[1]) < 0:
                invalid.append(i + 1)
        return sum(invalid)

    else:
        first = [[2]]
        second = [[6]]
        packets.append(first)
        packets.append(second)
        s = sorted(packets, key=cmp_to_key(compare))

        return (s.index(first) + 1) * (s.index(second) + 1)
