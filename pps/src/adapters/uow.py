from pps.src.adapters.repository.spark.candle import SparkCandleRepository
from pps.src.adapters.repository.tinkoff.market import TinkoffMarketRepository
from pps.src.domain.uow import AbstractUnitOfWork


class UnitOfWork(AbstractUnitOfWork):
    def __init__(self, market_client, spark_session, broker=None) -> None:
        self._market_client = market_client
        self._spark_session = spark_session
        self.market = TinkoffMarketRepository(self._market_client)
        self.candle = SparkCandleRepository(self._spark_session)
        self.broker = broker

    @property
    def market_client(self):
        return self._market_client

    @property
    def spark_session(self):
        return self._spark_session
