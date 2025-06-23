from datetime import timedelta
from pps.src.domain.candle import entity
from pps.src.domain.market import dto
from pps.src.domain.market.repository import AbstractMarketRepository
from tinkoff.invest import CandleInterval
from tinkoff.invest.schemas import CandleSource
from tinkoff.invest.utils import now


class TinkoffMarketRepository(AbstractMarketRepository):
    def __init__(self, client):
        self._client = client

    def get_candles(self, candle_request: dto.MarketCandleRequest) -> list[entity.Candle]:
        with self._client as client:
            candles = []
            for candle in client.get_all_candles(
                instrument_id=candle_request.token,
                from_=now() - timedelta(days=60),
                interval=CandleInterval.CANDLE_INTERVAL_DAY,
                candle_source_type=CandleSource.CANDLE_SOURCE_UNSPECIFIED,
            ):
                candles.append(candle)
        return [entity.Candle(
            token=candle_request.token,
            open=float(candle.open.units + candle.open.nano / 1000000000),
            high=float(candle.high.units + candle.high.nano / 1000000000),
            low=float(candle.low.units + candle.low.nano / 1000000000),
            close=float(candle.close.units + candle.close.nano / 1000000000),
            volume=float(candle.volume),
            timestamp=candle.time,
        ) for candle in candles]