# src/betynic/server.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .utils import calc_liability

app = FastAPI(title="Astrynn DevForge")

class LiabilityRequest(BaseModel):
    stake: float
    lay_odds: float
    commission_rate: float = 0.05
    volatility_adjustment: float = 1.0
    daily_interest: float = 1.0

class LiabilityResponse(BaseModel):
    liability: float

@app.post("/liability/", response_model=LiabilityResponse)
def compute_liability(req: LiabilityRequest):
    try:
        value = calc_liability(
            stake=req.stake,
            lay_odds=req.lay_odds,
            commission_rate=req.commission_rate,
            volatility_adjustment=req.volatility_adjustment,
            daily_interest=req.daily_interest
        )
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return {"liability": value}
