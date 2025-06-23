import abc

from datetime import datetime
from pps.src.domain.candle import entity


class AbstractCandleRepository(abc.ABC):
    @abc.abstractmethod
    def create(self, dto: list[entity.Candle]) -> None: ...

    @abc.abstractmethod
    def get(self, timestamp: datetime) -> list[entity.Candle]: ...
