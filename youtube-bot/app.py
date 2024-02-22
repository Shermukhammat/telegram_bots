from loader import dp, manager
from aiogram import executor
import logging, handlers
import asyncio


async def on_startup(dispatcher):
    # await manager.start_music_managing()
    asyncio.create_task(manager.start_music_managing())
    # asyncio.create_task(manager.start_video_managing())
     

if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    executor.start_polling(dp, skip_updates = False, on_startup = on_startup)
    # executor.start_webhook(dp, )