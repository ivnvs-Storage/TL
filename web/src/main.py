from typing import Annotated
from fastapi import Depends, FastAPI, APIRouter
from datetime import datetime
from pps.src.aplication.schemas import UpdateCandlesRequest
from pps.src.aplication.usecase import Usecase, QueryUsecase
from pps.src.deps import make_usecase, make_query_usecase
from pps.src.domain.candle import entity
from web.src import schemas

app = FastAPI()

router_price_processing = APIRouter(prefix="/price", tags=["price"])
router_strategy = APIRouter(prefix="/strategy", tags=["strategy"])


@router_price_processing.get("/candles/{token}")
async def get_candles(
    token: str,
    usecase: Annotated[Usecase, Depends(make_usecase)],
) -> list[schemas.CandleData]:
    """
    Get candles data for the specified time period.<br>

    Args: <br>
        token (BBG004730N88): Trading instrument identifier<br>

    Returns:<br>
        list[CandleData]
    """
    candles = usecase.get_candles_for_token(token)
    return [
        schemas.CandleData(
            open=candle.open,
            high=candle.high,
            low=candle.low,
            close=candle.close,
            volume=candle.volume,
            timestamp=candle.timestamp,
        ) for candle in candles
    ]

@router_price_processing.get("/send/candles/{token}")
async def send_candles(
    token: str,
    usecase: Annotated[Usecase, Depends(make_usecase)],
) -> list[schemas.CandleData]:
    """
    Update candles data for the specified trading instrument.<br>

    Args:<br>
        token (BBG004730N88): Trading instrument identifier<br>
    """
    candles = usecase.get_candles_for_token(token)
    await usecase.send_candles_async(candles)
    return [
        schemas.CandleData(
            open=candle.open,
            high=candle.high,
            low=candle.low,
            close=candle.close,
            volume=candle.volume,
            timestamp=candle.timestamp,
        ) for candle in candles
    ]

@router_price_processing.patch("/update")
async def update_candles(
    token: str,
    start_date: datetime,
    end_date: datetime,
    usecase: Annotated[Usecase, Depends(make_usecase)],
):
    """
    Update price data for the specified trading instrument.<br>

    Args:<br>
        token (str): Trading instrument identifier<br>
        start_date (datetime): Start date for the update<br>
        end_date (datetime): End date for the update<br>

    Returns:<br>
        dict: Operation status<br>
    """
    usecase.update_candles(UpdateCandlesRequest(
        token=token,
        start_time=start_date,
        end_time=end_date,
    ))
    return {"status": "success", "message": f"Цены для {token} обновлены"}

# Эндпоинты для стратегий
@router_strategy.get("/balance")
async def get_balance():
    """
    Get current trading account balance.<br>

    Returns:<br>
        dict: Account balance and currency information
    """
    return {"balance": 10000.0, "currency": "USD"}

@router_strategy.get("/transactions")
async def get_transactions(
    start_date: datetime,
    end_date: datetime
) -> list[schemas.Transaction]:
    """
    Get transaction history for the specified period.<br>

    Args:<br>
        start_date (datetime): Start date of the period<br>
        end_date (datetime): End date of the period<br>

    Returns:<br>
        list[Transaction]
    """
    return [
        schemas.Transaction(
            id=1,
            timestamp=datetime.now(),
            type="BUY",
            amount=100.0,
            asset="BTC"
        )
    ]

@router_strategy.get("/active-strategies")
async def get_active_strategies() -> list[schemas.Strategy]:
    """
    Get list of active trading strategies.<br>

    Returns:<br>
        list[Strategy]
    """
    return [
        schemas.Strategy(
            id=1,
            name="Momentum Strategy",
            is_active=True,
            description="Торговля на основе импульса цены"
        )
    ]

@router_strategy.post("/activate/{strategy_id}")
async def activate_strategy(strategy_id: int):
    """
    Activate trading strategy by its identifier.<br>

    Args:<br>
        strategy_id (int): Strategy identifier<br>

    Returns:<br>
        dict: Operation status
    """
    return {"status": "success", "message": f"Стратегия {strategy_id} активирована"}

@router_strategy.post("/deactivate/{strategy_id}")
async def deactivate_strategy(strategy_id: int):
    """
    Deactivate trading strategy by its identifier.<br>

    Args:<br>
        strategy_id (int): Strategy identifier<br>

    Returns:<br>
        dict: Operation status
    """
    return {"status": "success", "message": f"Стратегия {strategy_id} деактивирована"}

# Подключаем роутеры к приложению
app.include_router(router_price_processing)
app.include_router(router_strategy)

