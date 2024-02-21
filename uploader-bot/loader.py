from aiogram import Bot, Dispatcher
from aiogram.bot.api import TelegramAPIServer



local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081')
bot = Bot(token = API_TOKEN, server = local_server)

dp = Dispatcher(bot)
db = DataBase()