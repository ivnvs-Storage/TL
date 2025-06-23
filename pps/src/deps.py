from faststream.rabbit import RabbitBroker
from pps.src.adapters.database.spark import make_spark_session
from pps.src.adapters.market.tinkoff import make_market_client
from pps.src.adapters.uow import UnitOfWork
from pps.src.aplication.usecase import QueryUsecase, Usecase
from pps.src.domain.candle.service import CandleService
from pps.src.domain.market.service import MarketService
from pps.src.adapters.message_broker import make_rabbit_broker


def make_broker() -> RabbitBroker:
    return make_rabbit_broker()

def make_usecase() -> Usecase:
    return Usecase(
        uow=UnitOfWork(
            market_client=make_market_client(),
            spark_session=make_spark_session(),
            broker=make_broker()
        ),
        market_service=MarketService(),
        candle_service=CandleService(),
    )

def make_query_usecase() -> QueryUsecase:
    return QueryUsecase(make_market_client(), make_spark_session())
