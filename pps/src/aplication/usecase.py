from pps.src.aplication.schemas import UpdateCandlesRequest
from pps.src.domain.candle.service import CandleService
from pps.src.domain.market.dto import MarketCandleRequest
from pps.src.domain.market.service import MarketService
from pps.src.domain.uow import AbstractUnitOfWork
from pps.src.domain.candle import entity


class Usecase:
    def __init__(
        self,
        uow: AbstractUnitOfWork,
        market_service: MarketService,
        candle_service: CandleService,
    ) -> None:
        self._uow: AbstractUnitOfWork = uow
        self._market_service: MarketService = market_service
        self._candle_service: CandleService = candle_service
        self._broker = getattr(uow, 'broker', None)

    def update_candles(
        self,
        dto: UpdateCandlesRequest,
    ) -> None:
        candles = self._market_service.get_candles(self._uow, MarketCandleRequest(
            token=dto.token,
            start_time=dto.start_time,
            end_time=dto.end_time,
        ))
        self._candle_service.create_candles(self._uow, candles)

    def send_candles(self):
        # Получаем свечи из spark
        candles = self._uow.candle.get_all()
        # Отправляем в очередь RabbitMQ через faststream
        if self._broker is not None:
            for candle in candles:
                self._broker.publish(candle.model_dump(), queue_name="candles")
        return candles

    def get_candles_for_token(self, token: str) -> list[entity.Candle]:
        return [c for c in self._uow.candle.get_all() if c.token == token]

    async def send_candles_async(self, candles: list[entity.Candle]):
        if self._broker is not None:
            async with self._broker:
                for candle in candles:
                    await self._broker.publish(candle.model_dump(), queue="candles")
        return candles

class QueryUsecase:
    def __init__(self, market_client, session) -> None:
        self._spark_session = session
        self._tinkoff_client = market_client

    def get_candles(self) -> list[entity.Candle]:
        df = self._spark_session.read.parquet("/Users/alexeyivanov/Desktop/TL/pps/src/adapters/repository/tinkoff/data")
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
