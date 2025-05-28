import pytest
from math import isclose

from src.betynic.utils import calc_liability
from betynic.utils import calc_liability


def test_calc_liability_default():
    result = calc_liability(100, 3.0)
    assert isclose(result, 10.0, rel_tol=1e-9)


def test_calc_liability_custom_commission():
    result = calc_liability(50, 4.0, commission_rate=0.1)
    assert isclose(result, 15.0, rel_tol=1e-9)


def test_calc_liability_with_adjustments():
    result = calc_liability(
        stake=75,
        lay_odds=2.5,
        commission_rate=0.07,
        volatility_adjustment=1.2,
        daily_interest=1.01,
    )
    expected = 75 * (2.5 - 1) * 0.07 * 1.2 * 1.01
    assert isclose(result, expected, rel_tol=1e-9)
