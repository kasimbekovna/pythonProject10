from aiogram import Router, types
from bot import bot
from aiogram.types import ReplyKeyboardRemove

 
echo_router = Router()


@echo_router.message()
async def echo(message: types.Message):
    chat_id = message.from_user.id
    text = message.text
    await bot.send_message(chat_id=chat_id, text=text, reply_markup=ReplyKeyboardRemove())

