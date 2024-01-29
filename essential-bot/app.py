import logging, handlers
from aiogram import executor
from loader import dp 




if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp)