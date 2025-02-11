from datetime import datetime
from pydantic import BaseModel


class CandleData(BaseModel):
    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float

class Strategy(BaseModel):
    id: int
    name: str
    is_active: bool
    description: str

class Transaction(BaseModel):
    id: int
    timestamp: datetime
    type: str
    amount: float
    asset: str