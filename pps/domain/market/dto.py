from datetime import datetime
from pydantic import BaseModel


class UpdateCandles(BaseModel):
    token: str
    start_time: datetime
    end_time: datetime
