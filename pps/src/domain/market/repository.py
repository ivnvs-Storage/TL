import abc

from pps.src.domain.market import dto
from pps.src.domain.candle import entity


class AbstractMarketRepository(abc.ABC):
    @abc.abstractmethod
    def get_candles(self, candle_request: dto.MarketCandleRequest) -> list[entity.Candle]: ...
