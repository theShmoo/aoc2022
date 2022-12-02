"""day02 of aoc2022"""
from os.path import dirname, join

DATA = "input.txt"


def load_lines():
    """loads all lines of the given file as an array of strings."""

    script_dir = dirname(__file__)
    with open(join(script_dir, DATA), encoding='utf-8') as file:
        return file.read().splitlines()


def calc_points_level_1(enemy, you):
    """calculate the points of a single game."""
    draw = 3
    win = 6

    points = you + 1

    # draw
    if enemy == you:
        return points + draw

    # lose
    if (enemy - 1) % 3 == you:
        return points

    # win
    return points + win


def calc_points(game, level):
    """calculates the points of a single game for the given level."""
    enemy, you = game

    if level == 1:
        move = you
    else:
        move = ((enemy + you - 1) % 3)

    return calc_points_level_1(enemy, move)


def solve(level):
    """solve for a specified number of elves."""

    games = [(ord(line[0]) - ord('A'), ord(line[2]) - ord('X'))
             for line in load_lines()]

    points = sum(calc_points(r, level) for r in games)

    return points


def solve_1():
    """solve part 1."""

    print(solve(1))


def solve_2():
    """solve part 2."""

    print(solve(2))
