from aiogram import Bot, Dispatcher
from settings import settings
from aiogram.client.bot import DefaultBotProperties

dp = Dispatcher()
bot = Bot(settings.BOT_TOKEN, default=DefaultBotProperties(parse_mode='HTML'))


@dp.startup()
async def startup():
    me = await bot.get_me()
    print(f"Bot started on {me.username}")


@dp.shutdown()
async def shutdown():
    print(f"Bot stopped")
