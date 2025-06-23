from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MarketCandleRequest(BaseModel):
    token: str
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
