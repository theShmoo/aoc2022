"""day01 of aoc2022"""
from itertools import groupby


def solve_for_elves(num_elves, data):
    """solve for a specified number of elves."""

    elves_str = [list(g) for k, g in groupby(data, lambda s: s != "")]
    sum_calories = [sum(int(y) for y in x) for x in elves_str if x[0] != ""]
    sum_calories.sort()
    return sum(sum_calories[-num_elves:])


def solve(part, data):
    """solve day01 for the given part and data."""
    if part == 1:
        return solve_for_elves(1, data)
    return solve_for_elves(3, data)
