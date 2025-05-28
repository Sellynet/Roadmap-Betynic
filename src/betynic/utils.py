def calc_liability(
    stake: float,
    lay_odds: float,
    commission_rate: float = 0.05,
    volatility_adjustment: float = 1.0,
    daily_interest: float = 1.0,
) -> float:
    """Calcula la liability de una apuesta lay."""
    if lay_odds <= 1:
        raise ValueError("lay_odds debe ser > 1")
    return (
        stake
        * (lay_odds - 1)
        * commission_rate
        * volatility_adjustment
        * daily_interest
    )
  
