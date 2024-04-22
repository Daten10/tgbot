import asyncio
import logging
from aiogram import Bot


from config import bot, dp, set_my_menu, database
from handlers.start import start_router
from handlers.review import review_router
from handlers.menu import menu_router
from handlers.generic_answer import echo_router


async def on_startup(bot: Bot):
    await database.create_tables()


async def main():

    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(review_router)
    dp.include_router(echo_router)

    dp.startup.register(on_startup)
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
