"""usage: ./aoc_2022 -h"""

import argparse
import importlib
import time
from aoc_2022.utils import load_lines


def tic_toc_fmt(tic, toc):
    """format the time measurements."""
    return f'{toc - tic:0.4f} seconds'


def solve_part(day_str, part, data, profiling):
    """solve the specified part of the specified day."""

    part_str = f'{day_str} part {part}'

    print(f'-- solving {part_str}')
    day_module = importlib.import_module(f'aoc_2022.{day_str}')
    solve = getattr(day_module, day_str)

    tic = time.perf_counter()
    print(f'>> result: {solve(part, data)}')
    toc = time.perf_counter()

    if profiling:
        print(f'-- solved {part_str} in {tic_toc_fmt(tic, toc)}\n')


def solve_day(day, profiling):
    """solve the specified day."""

    day_str = f'day_{day:02d}'

    try:
        data = load_lines(day_str, False)
        solve_part(day_str, 1, data, profiling)
        solve_part(day_str, 2, data, profiling)

    except FileNotFoundError as e:
        print(f'-- unable to get data for {day_str}: [{e}]')
        return False
    except ImportError as e:
        print(f'-- unable to import {day_str}: [{e}]')
        return False

    return True


def solve_all_days(profiling):
    """solve all days."""

    print('++ solving all days\n')

    tic = time.perf_counter()
    for day in range(1, 5):
        if not solve_day(day, profiling):
            return False
    toc = time.perf_counter()

    if profiling:
        print(f'++ solved aoc 2022 in {tic_toc_fmt(tic, toc)}\n')

    return True


def parse_arguments(arguments):
    """parse the command line arguments"""

    parser = argparse.ArgumentParser(
        prog='aoc_2022',
        description='advent of code 2022',
        epilog='by theShmoo')
    parser.add_argument(
        '-d', '--day', type=int,
        help='solve a specific day. If not set solve all days')
    parser.add_argument(
        '-p', '--profile',
        action='store_true',
        help='add profiling output.')

    return parser.parse_args(arguments)


def start(arguments):
    """Entrypoint of aoc_2022."""

    args = parse_arguments(arguments)

    profiling = args.profile

    if args.day:
        return solve_day(args.day, profiling)

    return solve_all_days(profiling)
