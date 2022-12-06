"""usage: ./aoc_2022 -h"""

import argparse
import importlib
import time
from aoc_2022.utils import load_lines
from io import StringIO


possible_parts = [1, 2]
possible_days = range(1, 8)


def timing_fmt(tic, toc):
    """format the time measurements."""
    return f'{toc - tic:0.4f} seconds'


def solve_part(day_str, part, data, timing):
    """solve the specified part of the specified day."""

    part_str = f'{day_str} part {part}'

    print(f'-- solving {part_str}')
    day_module = importlib.import_module(f'aoc_2022.{day_str}')
    solve = getattr(day_module, day_str)

    tic = time.perf_counter()
    print(f'>> result: {solve(part, data)}')
    toc = time.perf_counter()

    if timing:
        print(f'-- solved {part_str} in {timing_fmt(tic, toc)}\n')


def solve_day(day, parts, timing, example):
    """solve the specified day."""

    day_str = f'day_{day:02d}'

    data = load_lines(day_str, example)
    for part in parts:
        solve_part(day_str, part, data, timing)


def solve_days(days, parts, timing, example):
    """solve the given days."""

    print('++ solving aoc 2022\n')

    tic = time.perf_counter()
    for day in days:
        solve_day(day, parts, timing, example)
    toc = time.perf_counter()

    if timing:
        print(f'++ solved aoc 2022 in {timing_fmt(tic, toc)}\n')


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(
            "%s is an invalid positive int value" % value)
    return ivalue


def make_parser():
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog='aoc_2022',
        description='advent of code 2022',
        epilog='by theShmoo')
    parser.add_argument(
        '-d', '--day', type=int, choices=possible_days,
        help='solve a specific day, if not set solve all days')
    parser.add_argument(
        '-p', '--part', type=int, choices=possible_parts,
        help='solve only for a specific part, if not set solve for all parts')
    parser.add_argument(
        '-t', '--timing',
        action='store_true',
        help='add timinig output')
    parser.add_argument(
        '-e', '--example',
        action='store_true',
        help='use example data')
    parser.add_argument(
        '-r', '--repeat',
        type=check_positive,
        default=1,
        help='repeat the execution several times')
    return parser


def parse_arguments(arguments):
    """parse the command line arguments"""

    return make_parser().parse_args(arguments)


def usage():
    f = StringIO()
    make_parser().print_help(f)
    return f.getvalue()


def start(arguments):
    """Entrypoint of aoc_2022."""

    args = parse_arguments(arguments)

    timing = args.timing
    example = args.example
    parts = [args.part] if args.part else possible_parts
    days = [args.day] if args.day else possible_days

    repeat = args.repeat
    if repeat > 1:
        print(f'## Repeating the execution {repeat} times')

    for r in range(1, repeat + 1):
        if repeat > 1:
            print(f'## run {r}')
        solve_days(days, parts, timing, example)

    return True
