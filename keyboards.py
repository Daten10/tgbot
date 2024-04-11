from aiogram import Router, types, F
from aiogram.filters import Command


def start_keyboard():
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[

            [
                types.InlineKeyboardButton(text='Наш сайт', url="https://mypizza.kg/"),
                types.InlineKeyboardButton(text='Инстаграм', url="https://www.instagram.com/mypizzakg/?hl=en")
            ],

            [
                types.InlineKeyboardButton(text='Контакты', callback_data='contacts'),
                types.InlineKeyboardButton(text='Адрес', callback_data='adress')
            ],

            [
                types.InlineKeyboardButton(text='Оставить отзыв', callback_data='review')
            ]

        ]
    )
    return keyboard

