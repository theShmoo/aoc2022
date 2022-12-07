"""tests for aoc 2022."""
from aoc_2022 import load_lines
from aoc_2022 import day_01, day_02, day_03, day_04, day_05, day_06, day_07


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
    assert day_03(1, data) == 157
    assert day_03(2, data) == 70


def test_day_03_real():
    """Test day 03 real input."""

    data = load_lines('day_03', False)
    assert day_03(1, data) == 7766
    assert day_03(2, data) == 2415


def test_day_04_example():
    """Test day 04 example input."""

    data = load_lines('day_04', True)
    assert day_04(1, data) == 2
    assert day_04(2, data) == 4


def test_day_04_real():
    """Test day 04 real input."""

    data = load_lines('day_04', False)
    assert day_04(1, data) == 487
    assert day_04(2, data) == 849


def test_day_05_example():
    """Test day 05 example input."""

    data = load_lines('day_05', True)
    assert day_05(1, data) == 'CMZ'
    assert day_05(2, data) == 'MCD'


def test_day_05_real():
    """Test day 05 real input."""

    data = load_lines('day_05', False)
    assert day_05(1, data) == 'ZWHVFWQWW'
    assert day_05(2, data) == 'HZFZCCWWV'


def test_day_06_example():
    """Test day 06 example input."""

    data = load_lines('day_06', True)
    assert day_06(1, data) == 7
    assert day_06(2, data) == 19


def test_day_06_real():
    """Test day 06 real input."""

    data = load_lines('day_06', False)
    assert day_06(1, data) == 1833
    assert day_06(2, data) == 3425


def test_day_07_example():
    """Test day 07 example input."""

    data = load_lines('day_07', True)
    assert day_07(1, data) == 95437
    assert day_07(2, data) == 24933642


def test_day_07_real():
    """Test day 07 real input."""

    data = load_lines('day_07', False)
    assert day_07(1, data) == 1490523
    assert day_07(2, data) == 12390492
