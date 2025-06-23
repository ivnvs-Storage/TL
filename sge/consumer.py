from faststream import FastStream, Logger
from faststream.rabbit import RabbitBroker, RabbitQueue
from pps.src.config import settings
from pps.src.domain.candle.entity import Candle

# Используем переменную окружения для подключения
broker = RabbitBroker(settings.RABBITMQ_URL)
app = FastStream(broker)

queue = RabbitQueue("candles")

@broker.subscriber(queue)
async def handle_candle(msg: dict, logger: Logger):
    candle = Candle(**msg)
    logger.info(f"Получена свеча: {candle}")

if __name__ == "__main__":
    import asyncio
    asyncio.run(app.run())