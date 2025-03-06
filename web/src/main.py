from fastapi import FastAPI, APIRouter
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from web.src import schemas

app = FastAPI()

router_price_processing = APIRouter(prefix="/price", tags=["price"])
router_strategy = APIRouter(prefix="/strategy", tags=["strategy"])


@router_price_processing.get("/candles")
async def get_candles(
    start_date: datetime,
    end_date: datetime,
    token: str,
    interval: str = "1h"
) -> list[schemas.CandleData]:
    """
    Get candles data for the specified time period.<br>

    Args: <br>
        start_date (datetime): Start date of the period<br>
        end_date (datetime): End date of the period<br>
        token (str): Trading instrument identifier<br>
        interval (str, optional): Candle interval. Defaults to "1h"<br>

    Returns:<br>
        list[CandleData]
    """
    return [
        schemas.CandleData(
            timestamp=datetime.now(),
            open=100.0,
            high=105.0,
            low=98.0,
            close=103.0,
            volume=1000.0
        )
    ]

@router_price_processing.patch("/update")
async def update_prices(
    token: str,
    start_date: datetime,
    end_date: datetime
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

