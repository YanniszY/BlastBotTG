import asyncio

from aiogram import Bot, Dispatcher, Router
from handlers.handlers import router
from handlers.handlers import register_handlers

from config import BOT_TOKEN

bot = Bot(BOT_TOKEN)
dp = Dispatcher()


register_handlers(dp, bot)

    
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())