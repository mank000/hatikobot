import asyncio
import logging
import os

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from database.models import async_main
from handlers.handlers import router

load_dotenv()

bot = Bot(token=os.environ.get("bot_key"))
dp = Dispatcher()


async def main():
    await async_main()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO
    )
    asyncio.run(main())
