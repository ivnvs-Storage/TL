from tinkoff.invest import Client
from pps.src.config import settings

TOKEN = settings.TINKOFF_TOKEN

def make_market_client() -> Client:
    return Client(TOKEN)