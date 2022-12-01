import argparse
import importlib


def solve_day(day):
    try:
        day_module = importlib.import_module(f'day{day:02d}.day{day:02d}')

        print(f'-- solving day{day:02d} part 1')

        day_module.solve_1()

        print(f'-- solving day{day:02d} part 2')

        day_module.solve_2()

    except ImportError:
        print(f'-- unable to import day{day:02d}')
        return False

    return True


def main():
    parser = argparse.ArgumentParser(
        prog='aoc2022',
        description='advent of code 2022',
        epilog='by theShmoo')
    parser.add_argument(
        '-d', '--day', type=int,
        help='solve a specific day. If not set solve all days')
    args = parser.parse_args()

    if args.day:
        return solve_day(args.day)
    else:
        print('-- solving all days')
        for day in range(1, 25):
            if not solve_day(day):
                return False


if __name__ == '__main__':
    if not main():
        exit(1)
