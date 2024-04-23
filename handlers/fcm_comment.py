from aiogram import Router, F, types
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from bot import database


comment_router = Router()

class Comments(StatesGroup):
    name = State()
    contacts = State()
    date = State()
    quality_food = State()
    clean = State()
    extra_comments = State()


@comment_router.callback_query(F.data == 'comment')
async def start_comment(callback: types.CallbackQuery, state: FSMContext):
    await callback.message.answer("Как вас зовут?")
    await state.set_state(Comments.name)


@comment_router.message(Comments.name)
async def load_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введите ваш номер телефона или Instagram.")
    await state.set_state(Comments.contacts)


@comment_router.message(Comments.contacts)
async def load_contacts(message: types.Message, state: FSMContext):
    await state.update_data(contacts=message.text)
    await message.answer("Введите дату вашего посещения (только цифры).")
    await state.set_state(Comments.date)


@comment_router.message(Comments.date)
async def lead_date(message: types.Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Как оцениваете качество еды от 1 до 10 бальной шкале")
    await state.set_state(Comments.quality_food)

@comment_router.message(Comments.quality_food)
async def lead_quality(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пожалуйста, введите дату в формате цифр.")
    elif not 1 <= int(message.text) <= 10:
        await message.answer("ставьте оценку от 1 до 10")
    else:
        await state.update_data(quality_food=int(message.text))
        await message.answer("Оцените чистоту нашего заведения")
        await state.set_state(Comments.clean)


@comment_router.message(Comments.clean)
async def load_clean(message: types.Message, state: FSMContext):
    if not message.text.isdigit():
        await message.answer("Пишите только числа")
    elif not 1 <= int(message.text) <= 10:
        await message.answer('ставьте оценку от 1 до 10')
    else:
        await state.update_data(clean=int(message.text))
        await message.answer("Есть ли у вас дополнительные комментарии?")
        await state.set_state(Comments.extra_comments)


@comment_router.message(Comments.extra_comments)
async def load_extra_comment(message: types.Message, state: FSMContext):
    await state.update_data(extra_comments=message.text)
    data = state.get_data()
    print("~", data)
    await database.execute(
        "INSERT INTO survey (name, contacts, date, quality_food, clean, EXTRA_COMMENTS) VALUES (?,?,?,?,?,?)",
        (data['name'], data['contacts'], data['date'], data['quality_food'], data['clean'], data['extra_comments']))
    await message.answer('Спасибо за ваш отзыв!\n'
                         'Всего доброго')
    await state.clear()
