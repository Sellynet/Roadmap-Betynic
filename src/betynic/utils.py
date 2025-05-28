# src/betynic/utils.py

def calc_liability(
    stake: float,
    lay_odds: float,
    commission_rate: float = 0.05,
    volatility_adjustment: float = 1.0,
    daily_interest: float = 1.0,
) -> float:
    """
    Calcula la liability de una apuesta lay.

    Args:
        stake (float): Monto apostado.
        lay_odds (float): Cuota lay (>1).
        commission_rate (float): Comisión del exchange (por defecto 5%).
        volatility_adjustment (float): Factor de ajuste por volatilidad.
        daily_interest (float): Tasa diaria (por defecto 1.0).

    Returns:
        float: Valor de liability ajustado.
    """
    if lay_odds <= 1:
        raise ValueError("lay_odds debe ser mayor que 1")
    return (
        stake
        * (lay_odds - 1)
        * commission_rate
        * volatility_adjustment
        * daily_interest
    )
