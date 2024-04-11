from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from os import getenv


load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


async def set_my_menu():
    await bot.set_my_commands(
        [
            types.BotCommand(command='start', description='начальное меню'),
            types.BotCommand(command='menu', description='меню блюд'),

        ]
    )