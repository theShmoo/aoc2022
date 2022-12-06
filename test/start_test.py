"""tests for aoc 2022."""
from aoc_2022 import start, usage
import pytest


def test_start():
    """Test starting with example data."""
    assert start(['-e'])


def test_start_with_timing():
    """Test starting with timing enabled."""
    assert start(['-t', '-d', '1'])


def test_start_day_01_part_01_with_timing():
    """Test starting with timing and part enabled."""
    assert start(['-d', '1', '-p', '1'])


def test_start_repeat_with_negativ_number():
    """Test starting with repeat and negativ number"""
    with pytest.raises(SystemExit):
        start(['-r', '0'])


def test_start_repeat():
    assert start(['-d', '1', '-p', '1', '-r', '2'])


def test_usage():
    assert 'usage: aoc_2022' in usage()
