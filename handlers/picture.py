from aiogram.filters import Command
from aiogram import Router, types
from aiogram.types import FSInputFile
import os
from random import choice


pic_router = Router()


@pic_router.message(Command('pic'))
async def pic(message: types.Message):
    path = 'media/tree-736885_1280.jpeg'
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='красивая фотка')


@pic_router.message(Command('pic_random'))
async def pic_random(message: types.Message):
    photos = os.listdir('media/')
    path = f'media/{choice(photos)}'
    print(photos)
    file = FSInputFile(path)
    await message.answer_photo(photo=file, caption='красивая фотка')


