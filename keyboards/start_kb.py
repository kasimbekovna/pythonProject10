from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def start_kb():
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='нащ адресс', callback_data='address'),
         InlineKeyboardButton(text='наш сайт', url='https://www.vecteezy.com/free-photos')],
        [InlineKeyboardButton(text='наше меню', callback_data='menu')]
    ])
    return kb

