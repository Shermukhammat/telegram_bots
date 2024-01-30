import logging, os

from aiogram import Bot, Dispatcher, executor, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.types import ContentType



# Configure logging
logging.basicConfig(level=logging.INFO)

# Create private Bot API server endpoints wrapper
local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081')

# Initialize bot with using local server
bot = Bot(token=API_TOKEN)
# ... and dispatcher
dp = Dispatcher(bot)


@dp.message_handler(commands = "start")
async def echo(update: types.Message):
     with open("test.mp4", "rb") as video_file:
        await bot.send_video(update.from_user.id, video_file, caption = "This is video bigger then 50 mb. That was amaizing!")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)