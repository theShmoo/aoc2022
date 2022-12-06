"""day 06 of aoc2022"""


def day_06(part, data):
    """solve day 06 for the given part and data."""

    chars = [*data[0]]

    marker_size = 4 if part == 1 else 14
    marker = chars[:marker_size]

    for i, c in enumerate(chars[marker_size:]):
        marker.pop(0)
        marker.append(c)

        if len(set(marker)) == marker_size:
            return marker_size + i + 1
