import asyncio
import logging
from aiogram import Bot, Dispatcher
from config_reader import config
from handlers import admin, user
from database.admin_db import db_start
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(token=config.token.get_secret_value(), parse_mode='HTML')


async def main():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=config.token.get_secret_value(), parse_mode='HTML')
    dp = Dispatcher(storage=MemoryStorage())
    await db_start()
    dp.include_routers(admin.router, user.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
