from aiogram import Bot, Dispatcher, types
from aiogram.bot.api import TelegramAPIServer
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import API_TOKEN, DATA_CHANEL
from data.base import DataBase 
from utilits.context import ConText
from utilits.buttons import Buttons, Inline
from utilits.states import States
from downloader.manager import FinishedTaskManger
from downloader.helpers import Tasks
from youtuba.base import YouTuba


# local_server = TelegramAPIServer.from_base('http://127.0.0.1:8081')http://127.1.1.1:7070
storage = MemoryStorage()


bot = Bot(token = API_TOKEN)
dp = Dispatcher(bot, storage = storage)

db = DataBase()
context = ConText()
buttons = Buttons()
inline = Inline()

states = States()
ytb = YouTuba(downloanding_limit = 1_500)
# queues = Queue()
manager = FinishedTaskManger(bot, db = db, data_chanel = DATA_CHANEL)
tasks = Tasks(api_url = "http://127.1.1.1:7070")



