"""utility methods for aoc2022"""
from os.path import dirname, join


def load_lines(day_str, example):
    """loads all lines of the given level as a list of strings."""

    script_dir = dirname(__file__)
    file = "example.txt" if example else "input.txt"
    with open(join(script_dir, day_str, file), encoding='utf-8') as file_handle:
        return file_handle.read().splitlines()
