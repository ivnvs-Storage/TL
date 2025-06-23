import abc

from pps.src.domain.candle.repository import AbstractCandleRepository
from pps.src.domain.market.repository import AbstractMarketRepository


class AbstractUnitOfWork(abc.ABC):
    market: AbstractMarketRepository
    candle: AbstractCandleRepository
