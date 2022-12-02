"""tests for aoc 2022."""
import pytest
from src import *


def test_day01_example():
    """Test day 1 example input."""

    data = load_lines('day01', True)
    assert day01.solve.solve(1, data) == 24000
    assert day01.solve.solve(2, data) == 45000


def test_day01_real():
    """Test day 1 real input."""

    data = load_lines('day01', False)
    assert day01.solve.solve(1, data) == 66719
    assert day01.solve.solve(2, data) == 198551


def test_day02_example():
    """Test day 2 example input."""

    data = load_lines('day02', True)
    assert day02.solve.solve(1, data) == 15
    assert day02.solve.solve(2, data) == 12


def test_day02_real():
    """Test day 2 real input."""

    data = load_lines('day02', False)
    assert day02.solve.solve(1, data) == 9759
    assert day02.solve.solve(2, data) == 12429
