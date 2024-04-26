from aiogram import Router, F, types
from aiogram.filters import Command
from config import database

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


category = ['пиццы', 'горячие блюда', 'гарниры', 'напитки']


@menu_router.message(F.text.lower().in_(category))
async def show_horror(message: types.Message):
    categ = message.text.lower()
    print(categ)
    kb = types.ReplyKeyboardRemove()
    data = await database.fetch(
        """
        SELECT dishes.* FROM dishes 
        JOIN categories ON dishes.category_id = categories.id
        WHERE categories.name = ?
        """,
        (categ,),
        fetch_type='all'
    )
    if not data:
        await message.answer('По вашему запросу ничего не найдено', reply_markup=kb)
    await message.answer(f'Все наши блюда категории {categ}:')
    for dish in data:
        price = dish['price']
        name = dish['name']
        photo = types.FSInputFile(dish['picture'])
        keyboard = types.InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    types.InlineKeyboardButton(text='Заказать', callback_data='order_'),
                ]
            ]
        )
        await message.answer_photo(
            photo=photo,
            caption=f'Название блюда: {name}\nЦена: {price} сом',
            reply_markup=keyboard

        )


@menu_router.callback_query(F.data.startswith('order_'))
async def shop_order(callback: types.CallbackQuery):
    await callback.answer('Добавлено в корзину!')
