"""
Módulo de utilidades de Betynic.

Aquí van funciones genéricas para el engine de apuestas lay,
cálculos de liability, gestión de stakes, etc.
"""

def calc_liability(
    stake: float,
    lay_odds: float,
    commission_rate: float = 0.05,
    volatility_adjustment: float = 1.0,
    daily_interest: float = 1.0,
) -> float:
    """
    Calcula la liability de una apuesta lay.

    El cálculo básico es:
        liability = stake * (lay_odds - 1) * commission_rate
    y luego se ajusta por volatilidad e interés diario.

    Args:
        stake (float): Monto apostado.
        lay_odds (float): Cuota lay. Debe ser > 1.
        commission_rate (float): Comisión del exchange (por defecto 5%).
        volatility_adjustment (float): Factor de ajuste por volatilidad.
        daily_interest (float): Tasa diaria (por defecto 1.0).

    Returns:
        float: Valor de liability ajustado.

    Raises:
        ValueError: Si `lay_odds <= 1`, pues no tendría sentido apostar lay
                    a una cuota menor o igual a 1.
    """
    if lay_odds <= 1:
        raise ValueError("lay_odds debe ser mayor que 1")

    liability = (
        stake
        * (lay_odds - 1)
        * commission_rate
        * volatility_adjustment
        * daily_interest
    )
    return liability
