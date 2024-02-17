import pytz
from datetime import datetime
import time

class Queue:
    def __init__(self, attemp_count : int = 120, sleep_time : int = 5):
        self.attemp_count = attemp_count
        self.sleep_time = sleep_time
        
        self.video_queue = []
        self.music_queue = []
        
    def now(self, zone : str = 'Asia/Tashkent'):
        zone_tz = pytz.timezone(zone)
        zone_time = datetime.now(zone_tz)

        return zone_time #.strftime(f"%d.%m.%Y %H:%M")
        
    def remove_music_queue(self, id : int):
        if id in self.music_queue:
            self.music_queue.remove(id)
            return True 
    
    def add_music_queue(self, id : int):
        self.music_queue.append(id)
        
    
    def is_music_queue(self, id : int):
        if len(self.music_queue) >= 1 and self.music_queue[0] == id:
            return True
    
    
    def remove_video_queue(self, id : int):
        if id in self.video_queue:
            self.video_queue.remove(id)
            return True 
    
    def add_video_queue(self, id : int):
        self.video_queue.append(id)
    
    def is_video_queue(self, id : int):
        if len(self.video_queue) >= 1 and self.video_queue[0] == id:
            return True
    

# qu = Queue()
# start = qu.now()
# time.sleep(1)
# end = qu.now()

# print(start < end)