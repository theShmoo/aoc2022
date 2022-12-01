from itertools import groupby
from os.path import dirname, join

DATA = "input.txt"


def load_lines():
    script_dir = dirname(__file__)
    with open(join(script_dir, DATA)) as f:
        return f.read().splitlines()


def solve(num_elves):
    data = load_lines()
    elves_str = [list(g) for k, g in groupby(data, lambda s: s != "")]
    sum_calories = [sum([int(y) for y in x]) for x in elves_str if x[0] != ""]
    sum_calories.sort()
    return sum(sum_calories[-num_elves:])


def solve_1():
    print(solve(1))


def solve_2():
    print(solve(3))
