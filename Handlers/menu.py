from aiogram import Router, F, types
from aiogram.filters import Command


menu_router = Router()


@menu_router.message(Command('menu'))
async def shop(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Пиццы'),
                types.KeyboardButton(text='Горячие блюда')
            ],
            [
                types.KeyboardButton(text='Гарниры'),
                types.KeyboardButton(text='Напитки')
            ],
        ], resize_keyboard=True
    )
    await message.answer('Меню:', reply_markup=kb)


@menu_router.callback_query(F.data.startswith('order_'))
async def shop_order(callback: types.CallbackQuery):
    await callback.answer('Добавлено в корзину!')


@menu_router.message(F.text.lower() == 'пиццы')
async def pizza_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Заказать', callback_data='order_1'),
            ]
        ]
    )
    file = types.FSInputFile("D:/pyProjects/pythonProject/pics/Medium.png")
    await message.answer_photo(photo=file, caption='Пицца куриная 35см', reply_markup=keyboard)


@menu_router.message(F.text.lower() == 'гарниры')
async def pizza_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Заказать', callback_data='order_2'),
            ]
        ]
    )
    file = types.FSInputFile("D:/pyProjects/pythonProject/pics/fry.png")
    await message.answer_photo(photo=file, caption='Картошка фри', reply_markup=keyboard)


@menu_router.message(F.text.lower() == 'горячие блюда')
async def pizza_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Заказать', callback_data='order_3'),
            ]
        ]
    )
    file = types.FSInputFile("D:/pyProjects/pythonProject/pics/soup.png")
    await message.answer_photo(photo=file, caption='Китайский суп', reply_markup=keyboard)


@menu_router.message(F.text.lower() == 'напитки')
async def pizza_order(message: types.Message):
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text='Заказать', callback_data='order_4'),
            ]
        ]
    )
    file = types.FSInputFile("D:/pyProjects/pythonProject/pics/juice.png")
    await message.answer_photo(photo=file, caption='Лимонад', reply_markup=keyboard)

