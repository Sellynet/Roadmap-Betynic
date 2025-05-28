from fastapi import FastAPI
from pydantic import BaseModel
from src.betynic.utils import calc_liability

app = FastAPI(title="Betynic Liability API")


class LiabilityRequest(BaseModel):
    stake: float
    lay_odds: float
    commission_rate: float = 0.05
    volatility_adjustment: float = 1.0
    daily_interest: float = 1.0


class LiabilityResponse(BaseModel):
    liability: float


@app.post("/liability/", response_model=LiabilityResponse)
async def compute_liability(req: LiabilityRequest):
    """
    Calcula la liability de una apuesta a partir de los parámetros enviados.
    ---
    Request body:
    {
      "stake": 100.0,
      "lay_odds": 3.0,
      "commission_rate": 0.05,
      "volatility_adjustment": 1.0,
      "daily_interest": 1.0
    }
    """
    liab = calc_liability(
        stake=req.stake,
        lay_odds=req.lay_odds,
        commission_rate=req.commission_rate,
        volatility_adjustment=req.volatility_adjustment,
        daily_interest=req.daily_interest,
    )
    return LiabilityResponse(liability=liab)
