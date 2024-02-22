# from utilits.queue import Queue
# from aiogram import Bot, Dispatcher
import asyncio
# from pytube import YouTube
# from youtuba.base import YouTuba
# from youtuba.helpers import slugify, write_log, remove_file
# from data.base import DataBase
import requests


class Manager:
    def __init__(self, sleep_time : int = 5, long_sleep : int = 15, api_url : str = "http://127.1.1.1:7070"):
        self.sleep = sleep_time 
        self.long_sleep = long_sleep
        self.api_url = api_url
        # self.dp = dp
        # self.bot = bot 
        # self.ytb = ytb
    
    async def start_task_managing(self):    
        n = 0
        while True:
            n+=1
            print(n)
            
            data = self.get_task(self.api_url)
            
            if data and data.get('status'):
                print(data)
                if data.get('type') == 'music':
                    pass
                    
                elif data.get('type') == 'video':
                    pass
                
                else:
                    await asyncio.sleep(self.sleep)
                        
            else:
                await asyncio.sleep(self.sleep)
    
    
    def get_task(self, api_url : str) -> dict:
        try:
            respons = requests.get(f"{api_url}/getTask")

        except requests.exceptions.ConnectionError:
            print("API doesn't answer")
            return
            
        except:
            print("Somthing went wrong with API")
            return 
        
        if respons.status_code == 200:
            return respons.json()

        
            
            # data = self.queues.get_music_queue()
            
            # if data:
            #     print(data)
            #     try:
            #         yt = YouTube(f"https://www.youtube.com/watch?v={data['music_id']}", use_oauth = True)
            #         yt.check_availability()
            #         title = slugify(yt.title)
            #     except Exception as e:
            #         write_log(file_path = 'data/logs/manger.log', log = f"start_music_managing line 37: {data['music_id']} \nERROR: {e}")
            #         self.db.open_user_downlonding(data['user_id'])
            #         continue
                    
            #     try:
            #         status = await self.ytb.download_music(yt, title = title)
            #         if status:
            #             message = await self.bot.send_audio(chat_id = self.db.data['data_chanel'], audio = open(f'data/{title}.mp3', 'rb'), caption = yt.title)
                            
            #             await self.bot.copy_message(chat_id = data['user_id'], from_chat_id = self.db.data['data_chanel'], message_id = message.message_id)
            #             self.db.add_youtube_music(id = data['music_id'], data_id = message.message_id)
            #             self.db.open_user_downlonding(data['user_id'])
            #             remove_file(title+'.mp3')
                        
            #     except Exception as e:
            #         write_log(file_path = 'data/logs/manger.log', log = f"start_music_managing line 49: {data['music_id']} \nERROR: {e}")
            #         self.db.open_user_downlonding(data['user_id'])
            #         remove_file(title+'.mp3')
                        
                           
                    # else:
                    #     await self.bot.send_message(chat_id = data['user_id'], text = "Musiqani yuklab olib bo'lmadi")
                
                # except:
                    
                #     await self.bot.send_message(chat_id = data['user_id'], text = "Musiqani yuklab olib bo'lmadi")
            # else:
                # await asyncio.sleep(self.sleep)
    
    # async def start_video_managing(self):
    #     n = 0
    #     while True:
    #         n+=1
    #         print(n)
    #         data = self.queues.get_video_queue()
    #         if data:
    #             print(data)
            
    #         else:
    #             await asyncio.sleep(self.sleep)
                
                
# if __name__ == '__main__':
#     respons = requests.get("http://127.1.1.1:7070/getTask")
#     if respons.status_code == 200:
#         print(respons.json())
