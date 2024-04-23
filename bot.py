from aiogram.enums import ParseMode
from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from db.database import Database
from pathlib import Path

load_dotenv()
token = getenv('BOT_TOKEN')
bot = Bot(token=token)
dp = Dispatcher()

database = Database(
    Path(__file__).parent / "db.sglite"
)

