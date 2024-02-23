from aiogram import executor, Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer
import logging, asyncio
from config import DATA_CHANEL, API_TOKEN2 as API_TOKEN
from downloader.manager import Manager

local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081')

bot = Bot(API_TOKEN, server = local_server)
dp = Dispatcher(bot)
manager = Manager(bot, data_chanel = DATA_CHANEL, downloanding_limit = 1_500, sleep_time = 3)


# async def on_startup(dispatcher):
    # print("hi")
    # asyncio.create_task(manager.start_task_managing())



if __name__ == "__main__":
    # logging.basicConfig(level = logging.INFO)
    asyncio.run(manager.start_task_managing())
    # executor.start_polling(dp, skip_updates = False, on_startup = on_startup)