from datetime import datetime
from pps.src.domain.candle import entity
from pps.src.domain.candle.repository import AbstractCandleRepository
from pps.src.config import settings


class SparkCandleRepository(AbstractCandleRepository):
    def __init__(self, session):
        self._session = session

    def create(self, dto: list[entity.Candle]) -> None:
        if not dto:
            return
        df = self._session.createDataFrame([
            (c.token, c.open, c.high, c.low, c.close, c.volume, c.timestamp) for c in dto
        ], ["token", "open", "high", "low", "close", "volume", "timestamp"])
        df.write.mode("overwrite").parquet(settings.PARQUET_PATH)

    def get(self, timestamp: datetime) -> list[entity.Candle]:
        return []

    def get_all(self) -> list[entity.Candle]:
        df = self._session.read.parquet(settings.PARQUET_PATH)
        candles = []
        for row in df.collect():
            candle_data = {
                "token": row["token"],
                "open": row["open"],
                "high": row["high"],
                "low": row["low"],
                "close": row["close"],
                "volume": row["volume"],
                "timestamp": row["timestamp"]
            }
            candles.append(entity.Candle(**candle_data))
        return candles