import asyncio
from bot import bot, dp


import os
import sys

from handlers import routers

sys.path.append(os.getcwd())


async def start_bot():
    # await bot.set_my_commands(commands)
    await dp.start_polling(bot)


if __name__ == '__main__':
    for router in routers:
        dp.include_router(router)
    loop = asyncio.get_event_loop()
    loop.run_until_complete(start_bot())
