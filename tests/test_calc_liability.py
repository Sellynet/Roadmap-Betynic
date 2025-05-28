liability = (
    stake_amount
    * (lay_odds - 1)
    * exchange_commission_rate
    * adjustment_factor_for_market_volatility
    * daily_interest_rate
)
def calc_liability(
    stake: float,
    lay_odds: float,
    commission_rate: float = 0.05,
    volatility_adjustment: float = 1.0,
    daily_interest: float = 1.0,
) -> float:
    """Calcula la liability de una apuesta lay.

    Args:
        stake (float): Monto apostado.
        lay_odds (float): Cuota lay.
        commission_rate (float): Comisión del exchange (por defecto 5%).
        volatility_adjustment (float): Factor de ajuste por volatilidad.
        daily_interest (float): Tasa diaria (por defecto 1.0).

    Returns:
        float: Valor de liability ajustado.
    """
    return (
        stake
        * (lay_odds - 1)
        * commission_rate
        * volatility_adjustment
        * daily_interest
    )
import pytest
from math import isclose
from src.betynic.utils import calc_liability

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
Add initial unit tests for calc_liability
