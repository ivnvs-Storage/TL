from pps.src.domain.candle.entity import Candle
from pps.src.domain.market.dto import MarketCandleRequest
from pps.src.domain.uow import AbstractUnitOfWork
from pps.src.domain.price_processing.processing import prepare_candle_data


class MarketService:
    def get_candles(self, uow: AbstractUnitOfWork, candle_request: MarketCandleRequest) -> list[Candle]:
        candles = uow.market.get_candles(candle_request)
        return prepare_candle_data(candles)
