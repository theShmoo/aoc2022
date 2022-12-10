"""utility methods for aoc2022"""
from os.path import dirname, join, exists
from urllib.request import Request, urlopen
from os import environ


def get_input(path, year, day):

    cookie = environ['AOC_SESSION']
    url = f'https://adventofcode.com/{year}/day/{day}/input'

    request = Request(url, headers={
        'cookie': f'session={cookie}',
        'User-Agent': 'https://github.com/theShmoo/aoc2022'})
    input_bytes = urlopen(request).read()
    input_text = input_bytes.decode('utf-8')
    with open(path, 'w', encoding='utf-8') as input_file:
        input_file.write(input_text)
    return input_text


def load_lines(year, day, example):
    """loads all lines of the given level as a list of strings."""

    script_dir = dirname(__file__)
    input_dir = 'input'
    file_type = 'example.txt' if example else 'input.txt'
    input_file_name = f'day_{year}-{day}_{file_type}'
    path = join(script_dir, input_dir, input_file_name)

    if exists(path):
        with open(path, 'r', encoding='utf-8') as input_file:
            return input_file.read().splitlines()

    return get_input(path, year, day).splitlines()
