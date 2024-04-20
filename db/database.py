import aiosqlite
from db.queries import Queries

class Database:
    def __init__(self, path) -> None:
        self.path = path

    async def create_tables(self) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(Queries.CREATE_SURVEY_TABLE)
            # await db.execute(Queries.DROP_BOOKS_TABLE)
            await db.commit()

    async def execute(self, query: str, params: tuple | None = None) -> None:
        async with aiosqlite.connect(self.path) as db:
            await db.execute(query, params or ())
            await db.commit()

    async def insert_comments(self, name, contacts, date, quality_food, clean, extra_comments):
        async with aiosqlite.connect(self.path) as db:
            await db.execute(Queries.INSERT_COMMENTS(name, contacts, date, quality_food, clean, extra_comments))
            await db.commit()

