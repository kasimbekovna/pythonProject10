import asyncio
import logging
from bot import dp, db, database
from handlers import start_router, pic_router,callback_router, echo_router, menu_router,comment_router

async def on_startup():
    await database.create_tables()

async def main():
    dp.include_router(start_router)
    dp.include_router(pic_router)
    dp.include_router(callback_router)
    dp.include_router(menu_router)
    dp.include_router(comment_router)

    dp.startup.register(on_startapp)

    dp.include_router(echo_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
