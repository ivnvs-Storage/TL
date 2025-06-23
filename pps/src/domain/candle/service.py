from pps.src.domain.candle.entity import Candle
from pps.src.domain.uow import AbstractUnitOfWork


class CandleService:
    def create_candles(self, uow: AbstractUnitOfWork, candles: list[Candle]) -> None:
        return uow.candle.create(candles)