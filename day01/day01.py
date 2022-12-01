"""day01 of aoc2022"""
from itertools import groupby
from os.path import dirname, join

DATA = "input.txt"


def load_lines():
    """loads all lines of the given file as an array of strings."""

    script_dir = dirname(__file__)
    with open(join(script_dir, DATA), encoding='utf-8') as file:
        return file.read().splitlines()


def solve(num_elves):
    """solve for a specified number of elves."""

    data = load_lines()
    elves_str = [list(g) for k, g in groupby(data, lambda s: s != "")]
    sum_calories = [sum(int(y) for y in x) for x in elves_str if x[0] != ""]
    sum_calories.sort()
    return sum(sum_calories[-num_elves:])


def solve_1():
    """solve part 1."""

    print(solve(1))


def solve_2():
    """solve part 2."""

    print(solve(3))
