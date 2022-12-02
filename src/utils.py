"""utility methods for aoc2022"""
from os.path import dirname, join


def load_lines(day_str, example):
    """loads all lines of the given level as a list of strings."""

    script_dir = dirname(__file__)
    input_dir = 'input'
    file_type = 'example.txt' if example else 'input.txt'
    path = join(script_dir, input_dir, f'{day_str}_{file_type}')
    with open(path, encoding='utf-8') as handle:
        return handle.read().splitlines()
