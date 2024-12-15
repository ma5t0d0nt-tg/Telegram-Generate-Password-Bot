import asyncio
from aiogram import Bot, Dispatcher
from app import handlers_admin_bot, handlers_general, handlers_easter_eggs

from config.parser_config_admin import get_token

TOKEN = get_token()
bot = Bot(token=TOKEN)
dp = Dispatcher()


async def main():
    # добавление роутеров и запуск бота
    dp.include_routers(handlers_admin_bot.router,
                       handlers_general.router,
                       handlers_easter_eggs.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    finally:
        bot.session.close()
