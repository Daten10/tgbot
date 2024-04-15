from aiogram import Router, F, types
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from config import database

review_router = Router()


class UserReview(StatesGroup):
    name = State()
    phone_number = State()
    date = State()
    rate = State()
    clean = State()
    comment = State()


@review_router.callback_query(F.data == 'review')
async def start_review(cb: types.CallbackQuery, state: FSMContext):
    await cb.answer()
    await state.set_state(UserReview.name)
    await cb.message.answer('Как вас зовут?')


@review_router.message(UserReview.name)
async def process_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserReview.phone_number)
    await message.answer('Введите свой номер телефона')


@review_router.message(UserReview.phone_number)
async def process_phone_number(message: types.Message, state: FSMContext):
    number = message.text
    if not number.isdigit():
        await message.answer('Введите цифры!')
        return
    await state.update_data(phone_number=int(number))
    await state.set_state(UserReview.date)
    await message.answer('Введите дату посещения')


@review_router.message(UserReview.date)
async def process_date(message: types.Message, state: FSMContext):
    date = message.text
    if '.' not in date:
        await message.answer('Введите дату форматом "дд.мм.гггг"')
        return
    await state.update_data(date=date)
    await state.set_state(UserReview.rate)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='⭐'),
                types.KeyboardButton(text='⭐⭐⭐')
            ],
            [
                types.KeyboardButton(text='⭐⭐'),
                types.KeyboardButton(text='⭐⭐⭐⭐')
            ],
            [
                types.KeyboardButton(text='⭐⭐⭐⭐⭐')
            ]
        ], resize_keyboard=False
    )

    await message.answer('Оцените наше заведение', reply_markup=kb)


@review_router.message(UserReview.rate)
async def process_clean(message: types.Message, state: FSMContext):
    await state.update_data(rate=message.text)
    await state.set_state(UserReview.clean)
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text='Неудовлетворительно'),
                types.KeyboardButton(text='Удовлетворительно')
            ],
            [
                types.KeyboardButton(text='Хорошо'),
                types.KeyboardButton(text='Отлично')
            ]
        ], resize_keyboard=False
    )

    await message.answer('Оцените чистоту заведения', reply_markup=kb)


@review_router.message(UserReview.clean)
async def process_rate(message: types.Message, state: FSMContext):
    await state.update_data(clean=message.text)
    await state.set_state(UserReview.comment)
    kb = types.ReplyKeyboardRemove()
    await message.answer('Можете оставить дополнительный коментарий к отзыву!', reply_markup=kb)


@review_router.message(UserReview.comment)
async def process_comment(message: types.Message, state: FSMContext):
    kb = types.ReplyKeyboardRemove()
    await state.update_data(comment=message.text)
    data = await state.get_data()

    await database.execute(
        "INSERT INTO review (name, phone, date, rate, clean, comment) VALUES(?, ?, ?, ?, ?, ?)",
        (data['name'], data['phone_number'], data['date'], data['rate'], data['clean'], data['comment'])
    )
    await message.answer('Спасибо за ваш отзыв!\n/start\n/menu\n')
    await state.clear()

