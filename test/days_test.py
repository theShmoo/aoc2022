"""tests for aoc 2022."""
from aoc_2022 import load_lines
from aoc_2022 import day_01, day_02, day_03, day_04
from aoc_2022 import day_05, day_06, day_07, day_08
from aoc_2022 import day_09, day_10, day_11, day_12
from aoc_2022 import day_13, day_14


def test_day_01_example():
    """Test day 01 example input."""

    data = load_lines(2022, 1, True)
    assert day_01(1, data) == 24000
    assert day_01(2, data) == 45000


def test_day_01_real():
    """Test day 01 real input."""

    data = load_lines(2022, 1, False)
    assert day_01(1, data) == 66719
    assert day_01(2, data) == 198551


def test_day_02_example():
    """Test day 02 example input."""

    data = load_lines(2022, 2, True)
    assert day_02(1, data) == 15
    assert day_02(2, data) == 12


def test_day_02_real():
    """Test day 02 real input."""

    data = load_lines(2022, 2, False)
    assert day_02(1, data) == 9759
    assert day_02(2, data) == 12429


def test_day_03_example():
    """Test day 03 example input."""

    data = load_lines(2022, 3, True)
    assert day_03(1, data) == 157
    assert day_03(2, data) == 70


def test_day_03_real():
    """Test day 03 real input."""

    data = load_lines(2022, 3, False)
    assert day_03(1, data) == 7766
    assert day_03(2, data) == 2415


def test_day_04_example():
    """Test day 04 example input."""

    data = load_lines(2022, 4, True)
    assert day_04(1, data) == 2
    assert day_04(2, data) == 4


def test_day_04_real():
    """Test day 04 real input."""

    data = load_lines(2022, 4, False)
    assert day_04(1, data) == 487
    assert day_04(2, data) == 849


def test_day_05_example():
    """Test day 05 example input."""

    data = load_lines(2022, 5, True)
    assert day_05(1, data) == 'CMZ'
    assert day_05(2, data) == 'MCD'


def test_day_05_real():
    """Test day 05 real input."""

    data = load_lines(2022, 5, False)
    assert day_05(1, data) == 'ZWHVFWQWW'
    assert day_05(2, data) == 'HZFZCCWWV'


def test_day_06_example():
    """Test day 06 example input."""

    data = load_lines(2022, 6, True)
    assert day_06(1, data) == 7
    assert day_06(2, data) == 19


def test_day_06_real():
    """Test day 06 real input."""

    data = load_lines(2022, 6, False)
    assert day_06(1, data) == 1833
    assert day_06(2, data) == 3425


def test_day_07_example():
    """Test day 07 example input."""

    data = load_lines(2022, 7, True)
    assert day_07(1, data) == 95437
    assert day_07(2, data) == 24933642


def test_day_07_real():
    """Test day 07 real input."""

    data = load_lines(2022, 7, False)
    assert day_07(1, data) == 1490523
    assert day_07(2, data) == 12390492


def test_day_08_example():
    """Test day 08 example input."""

    data = load_lines(2022, 8, True)
    assert day_08(1, data) == 21
    assert day_08(2, data) == 8


def test_day_08_real():
    """Test day 08 real input."""

    data = load_lines(2022, 8, False)
    assert day_08(1, data) == 1713
    assert day_08(2, data) == 268464


def test_day_09_example():
    """Test day 09 example input."""

    data = load_lines(2022, 9, True)
    assert day_09(1, data) == 13
    assert day_09(2, data) == 1


def test_day_09_real():
    """Test day 09 real input."""

    data = load_lines(2022, 9, False)
    assert day_09(1, data) == 6563
    assert day_09(2, data) == 2653


def test_day_10_example():
    """Test day 10 example input."""

    data = load_lines(2022, 10, True)
    assert day_10(1, data) == 13140

    result = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""
    assert day_10(2, data) == result


def test_day_10_real():
    """Test day 10 real input."""

    data = load_lines(2022, 10, False)
    assert day_10(1, data) == 14540

    result = """
####.#..#.####.####.####.#..#..##..#####
.....#..#....#.#.......#.#..#.#..#....#.
###..####...#..###....#..####.#......#..
.....#..#..#...#.....#...#..#.#.....#...
#....#..#.#....#....#....#..#.#..#.#....
####.#..#.####.#....####.#..#..##..####.
"""
    assert day_10(2, data) == result


def test_day_11_example():
    """Test day 11 example input."""

    data = load_lines(2022, 11, True)
    assert day_11(1, data) == 10605
    assert day_11(2, data) == 2713310158


def test_day_11_real():
    """Test day 11 real input."""

    data = load_lines(2022, 11, False)
    assert day_11(1, data) == 107822
    assert day_11(2, data) == 27267163742


def test_day_12_example():
    """Test day 12 example input."""

    data = load_lines(2022, 12, True)
    assert day_12(1, data) == 31
    assert day_12(2, data) == 29


def test_day_12_real():
    """Test day 12 real input."""

    data = load_lines(2022, 12, False)
    assert day_12(1, data) == 339
    assert day_12(2, data) == 332


def test_day_13_example():
    """Test day 13 example input."""

    data = load_lines(2022, 13, True)
    assert day_13(1, data) == 13
    assert day_13(2, data) == 140


def test_day_13_real():
    """Test day 13 real input."""

    data = load_lines(2022, 13, False)
    assert day_13(1, data) == 6046
    assert day_13(2, data) == 21423


def test_day_14_example():
    """Test day 14 example input."""

    data = load_lines(2022, 14, True)
    assert day_14(1, data) == 24
    assert day_14(2, data) == 93


def test_day_14_real():
    """Test day 14 real input."""

    data = load_lines(2022, 14, False)
    assert day_14(1, data) == 779
    assert day_14(2, data) == 27426
