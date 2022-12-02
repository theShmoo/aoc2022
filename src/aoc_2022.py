"""usage: ./aoc2022 -h"""
import argparse
import importlib
import sys
import time
from utils import load_lines


def tic_toc_format(tic, toc):
    """format the time measurements."""
    return f'{toc - tic:0.4f} seconds'


def solve_part(day_str, part, data, profiling):
    """solve the specified part of the specified day."""

    print(f'-- solving {day_str} part {part}')
    day_module = importlib.import_module(day_str)
    solve = getattr(day_module, day_str)

    tic = time.perf_counter()
    print(f'>> result: {solve(part, data)}')
    toc = time.perf_counter()

    if profiling:
        print(
            f'-- solved {day_str} part {part} in {tic_toc_format(tic, toc)}\n')


def solve_day(day, profiling):
    """solve the specified day."""

    try:
        day_str = f'day_{day:02d}'
        data = load_lines(day_str, False)
        solve_part(day_str, 1, data, profiling)
        solve_part(day_str, 2, data, profiling)

    except ImportError as e:
        print(f'-- unable to import day{day:02d}: [{e}]')
        return False

    return True


def solve_all_days(profiling):
    """solve all days."""

    print('++ solving all days\n')

    tic = time.perf_counter()
    for day in range(1, 4):
        if not solve_day(day, profiling):
            return False
    toc = time.perf_counter()

    if profiling:
        print(f'++ solved aoc 2022 in {tic_toc_format(tic, toc)}\n')

    return True


def parse_arguments():
    """parse the command line arguments"""

    parser = argparse.ArgumentParser(
        prog='aoc2022',
        description='advent of code 2022',
        epilog='by theShmoo')
    parser.add_argument(
        '-d', '--day', type=int,
        help='solve a specific day. If not set solve all days')
    parser.add_argument(
        '-p', '--profile',
        action=argparse.BooleanOptionalAction,
        help='add profiling output.')

    return parser.parse_args()


def main():
    """Entrypoint of aoc2022."""

    args = parse_arguments()

    profiling = args.profile

    if args.day:
        return solve_day(args.day, profiling)

    return solve_all_days(profiling)


if __name__ == '__main__':
    if not main():
        sys.exit(1)
