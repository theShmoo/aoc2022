#!/bin/python

"""loads the aoc_2022 module and starts it."""

from aoc_2022 import start
import sys

if __name__ == '__main__':
    if not start(sys.argv[1:]):
        sys.exit(1)
