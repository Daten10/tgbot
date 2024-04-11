import asyncio
import logging


from config import bot, dp, set_my_menu
from Handlers.start import start_router
from Handlers.review import review_router
from Handlers.menu import menu_router
from Handlers.generic_answer import echo_router


async def main():

    await set_my_menu()
    dp.include_router(start_router)
    dp.include_router(menu_router)
    dp.include_router(review_router)
    dp.include_router(echo_router)

    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
