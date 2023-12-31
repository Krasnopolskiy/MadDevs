import asyncio

from loguru import logger

from services.binance import Binance
from services.bitfinex import Bitfinex


async def main():
    binance = Binance()
    bitfinex = Bitfinex()
    logger.info('Subscribe to receive updates from exchanges')
    await asyncio.gather(binance.subscribe(), bitfinex.subscribe())


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
