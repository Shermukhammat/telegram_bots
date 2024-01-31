from loader import dp 
from aiogram import executor
import logging, handlers



if __name__ == "__main__":
    logging.basicConfig(level = logging.INFO)
    executor.start_polling(dp, skip_updates = False)