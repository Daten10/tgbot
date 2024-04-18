from aiogram import Router, types, F
from aiogram.filters import Command
from keyboards import start_keyboard


start_router = Router()


@start_router.message(Command('start'))
async def start_cmd(message: types.Message):
    file = types.FSInputFile("D:/pyProjects/pythonProject/pics/imperia.jpg")
    await message.answer_photo(photo=file, reply_markup=start_keyboard(), caption='Добро пожаловать в империю пиццы!')


@start_router.callback_query(F.data == 'contacts')
async def about_us(callback: types.CallbackQuery):
    # await callback.answer('o nas')
    await callback.answer()
    await callback.message.answer_contact('+996 772 510 707\n', 'Империя Пиццы')
    await callback.message.answer_contact('+996 551 510 707\n', 'Империя Пиццы')


@start_router.callback_query(F.data == 'adress')
async def donate_us(callback: types.CallbackQuery):
    # await callback.answer('o nas')
    await callback.answer()
    await callback.message.answer('г.Бишкек, пр.Чуй, 92')


@start_router.callback_query(F.data == 'food')
async def menu(callback: types.CallbackQuery):

    await callback.answer('Блюда скоро появятся в меню!')

