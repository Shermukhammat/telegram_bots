from aiogram import Bot, Dispatcher, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN
from data.base import DataBase
from utilits.context import ConText
from utilits.buttons import Buttons, Inline
from utilits.states import States
from utilits.youtuba import YouTuba

local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081')
storage = MemoryStorage()


bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = DataBase()
context = ConText()
buttons = Buttons()
inline = Inline()

states = States()
ytb = YouTuba(videoSizeLimit = 500)