"""tests for aoc 2022."""
from aoc_2022 import start


def test_start():
    """Test starting without input."""
    assert start([])


def test_start_with_profiling():
    """Test starting with profiling enabled."""
    assert start(['-p'])


def test_start_day_01_with_profiling():
    """Test starting with profiling enabled."""
    assert start(['-p', '-d', '1'])


def test_start_day_26_should_fail():
    """Test starting day 26 which should fail."""
    assert not start(['-p', '-d', '26'])
