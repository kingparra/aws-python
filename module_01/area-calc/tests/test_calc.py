# test calculation of area and perim
import pytest

from area_calc import calc


def test_area():
    """Does area do multiplication on floats?"""
    assert calc.area(10, 34) == (10.0 * 34.0)


def test_perim():
    """Will perim use the right formula?"""
    assert calc.perim(10, 34) == (2 * (10.0 + 34.0))
