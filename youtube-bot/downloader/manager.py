from utilits.queue import Queue
from aiogram import Bot, Dispatcher
import asyncio


class Manager:
    def __init__(self, sleep : int = 3, dp : Dispatcher = None, bot : Bot = None, queues : Queue = None):
        self.sleep = sleep
        self.dp = dp
        self.bot = bot 
        self.queues = queues
    
    async def start_music_managing(self):
        n = 0
        while True:
            n+=1
            print(n)
            
            data = self.queues.get_music_queue()
            
            if data:
                print(data)
            
            else:
                await asyncio.sleep(self.sleep)
    
    # async def start_music_managing(self):
    #     while True:
    #         break