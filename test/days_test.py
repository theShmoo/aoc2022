"""tests for aoc 2022."""
from aoc_2022 import load_lines, day_01, day_02, day_03


def test_day_01_example():
    """Test day 01 example input."""

    data = load_lines('day_01', True)
    assert day_01(1, data) == 24000
    assert day_01(2, data) == 45000


def test_day_01_real():
    """Test day 01 real input."""

    data = load_lines('day_01', False)
    assert day_01(1, data) == 66719
    assert day_01(2, data) == 198551


def test_day_02_example():
    """Test day 02 example input."""

    data = load_lines('day_02', True)
    assert day_02(1, data) == 15
    assert day_02(2, data) == 12


def test_day_02_real():
    """Test day 02 real input."""

    data = load_lines('day_02', False)
    assert day_02(1, data) == 9759
    assert day_02(2, data) == 12429


def test_day_03_example():
    """Test day 03 example input."""

    data = load_lines('day_03', True)
    assert day_03(1, data) == 0
    assert day_03(2, data) == 0


def test_day_03_real():
    """Test day 03 real input."""

    data = load_lines('day_03', False)
    assert day_03(1, data) == 0
    assert day_03(2, data) == 0
