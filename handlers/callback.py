from aiogram.filters import Command
from aiogram import Router, types, F

callback_router = Router()

@callback_router.callback_query(F.data == 'address')
async def address(callback: types.CallbackQuery):
    await callback.message.answer(text = 'наш адресс : тут близко')
