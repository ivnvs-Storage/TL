from faststream.rabbit import RabbitBroker
from pps.src.config import settings

def make_rabbit_broker() -> RabbitBroker:
    return RabbitBroker(settings.RABBITMQ_URL) 