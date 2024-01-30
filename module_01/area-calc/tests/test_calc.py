# test calculation of area and perim
import pytest
from pint import UnitRegistry

from area_calc import calc

ureg = UnitRegistry()
Q = ureg.Quantity


def test_area():
    """Does area do multiplication on floats?"""
    assert calc.area("2m", "3.5m") == Q("7m")


def test_perim():
    """Will perim use the right formula?"""
    assert calc.perim("2m", "3.5m") == Q("9m")
