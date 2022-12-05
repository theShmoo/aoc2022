"""day 03 of aoc2022"""

lowercase_ord = ord('a')
uppercase_ord = ord('A')


def value_of_item(item):
    o = ord(item)
    if o >= lowercase_ord:
        return o - lowercase_ord + 1
    return o - uppercase_ord + 26 + 1


def day_03(part, data):
    """solve day 03 for the given part and data."""

    parts = []

    if part == 1:

        for line in data:
            size = int(len(line) / 2)
            first = set(line[:size])
            second = set(line[size:])
            parts.append(first.intersection(second).pop())
    else:
        chunk_size = 3

        for i in range(0, len(data), chunk_size):
            parts.append(set(data[i]).intersection(
                set(data[i+1])).intersection(set(data[i+2])).pop())

    return sum([value_of_item(p) for p in parts])
