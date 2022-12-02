"""day 02 of aoc2022"""


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


def day_02(level, data):
    """solve day 02 for the given part and data."""

    games = [(ord(line[0]) - ord('A'), ord(line[2]) - ord('X'))
             for line in data]

    points = sum(calc_points(r, level) for r in games)

    return points
