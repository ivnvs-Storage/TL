from datetime import datetime
from pydantic import BaseModel


class Candle(BaseModel):
    token: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    timestamp: datetime
