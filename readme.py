#!/bin/python
# -*- coding: utf-8 -*-

"""updates the readme."""

from os.path import dirname, join
import re
from aoc_2022 import usage


script_dir = dirname(__file__)
readme_path = join(script_dir, 'README.md')


def read_readme():
    with open(readme_path, encoding='utf-8') as handle:
        return handle.read()


def write_readme(to_write):
    with open(readme_path, encoding='utf-8', mode='w') as handle:
        handle.write(to_write)


def update_readme(num_stars, solved_days, usage):
    readme = read_readme()

    readme = re.sub(r'(day%20📅)-(\d+)', f'\\1-{solved_days}', readme)
    readme = re.sub(r'(stars%20⭐)-(\d+)', f'\\1-{num_stars}', readme)

    usage_start = '## Usage\n\n```'
    readme = readme[:readme.index(usage_start) + len(usage_start)]

    readme += f'man\n{usage}```\n'

    write_readme(readme)


if __name__ == '__main__':
    print('get the number of stars:')
    num_stars = input()

    print('get the solved days:')
    solved_days = input()

    usage = usage()

    update_readme(num_stars, solved_days, usage)
