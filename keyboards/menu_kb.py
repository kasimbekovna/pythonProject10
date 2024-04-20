from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def menu_kb():
    kb = ReplyKeyboardMarkup(keyboard=[
        [KeyboardButton(text='первые блюда--шорпо'),
         KeyboardButton(text='вторые блюда--плов')],
        [KeyboardButton(text='десерт--мороженое'),
         KeyboardButton(text='напитки--cola, pepsi, fanta')]
    ],
    one_time_keyboard=True,
    resize_keyboard=True)
    return kb