from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatchar
from db.database import Database
from pathlib import Path

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatchar()
database = Database(
    Path(__file__).parent / "db.sglite"
)

