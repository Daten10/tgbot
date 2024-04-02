import asyncio
import os

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from dotenv import load_dotenv
from os import getenv
import logging
from random import choice

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()
id_list = []


# handlers
@dp.message(Command('start'))
async def start_cmd(message: types.Message):
    if message.from_user.id not in id_list:
        id_list.append(message.from_user.id)
    await message.answer(f'Привет! {message.from_user.first_name}, '
                         f'наш бот обслуживает уже {len(id_list)} пользователя')


@dp.message(Command('myinfo'))
async def start_cmd(message: types.Message):
    img_dir = 'D:/pyProjects/pythonProject/pics'
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, choice(img_list))
    file = types.FSInputFile(img_path)
    await message.answer_photo(photo=file, caption=f'ваш id: {message.from_user.id} '
                                                   f'ваше имя: {message.from_user.first_name} '
                                                   f'ваш username: {message.from_user.username}')


@dp.message(Command('random_pic'))
async def send_picture(message: types.Message):
    img_dir = 'D:/pyProjects/pythonProject/pics'
    img_list = os.listdir(img_dir)
    img_path = os.path.join(img_dir, choice(img_list))
    file = types.FSInputFile(img_path)
    await message.answer_photo(photo=file)


@dp.message()
async def echo(message: types.Message):
    logging.info(message)
    await message.answer(message.text)


async def main():
    # запуск бота
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
