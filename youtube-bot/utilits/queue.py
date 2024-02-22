import pytz
from datetime import datetime
import time

class Queue:
    def __init__(self, sleep_time : int = 5):
        self.sleep_time = sleep_time
        
        self.video_queue = []
        self.music_queue = []
    
    def set_music_queue(self, user_id : int = None, music_id : str = None, message_id : int = None):
        self.music_queue.append({'user_id' : user_id, 'music_id' : music_id, 'message_id' : message_id})
        
    def get_music_queue(self):
        if len(self.music_queue) >= 1:
            return self.music_queue.pop(0)
    
    def set_video_queue(self, user_id : int = None, video_id : str = None, resolution : str = '144p'):
        self.video_queue.append({'user_id' : user_id, 'video_id' : video_id, 'resolution' : resolution})
        
    def get_video_queue(self):
        if len(self.video_queue) >= 1:
            return self.video_queue.pop(0)
        
    
    