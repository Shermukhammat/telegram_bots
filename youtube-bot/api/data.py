


class DataBase:
    def __init__(self):
        self.tasks = []
        self.finished_tasks = []
    
    async def addTask(self, task_type : str = 'type', ytid : str = None, resolution : str = '144p', messageId : int = None, userId : int = None) -> bool:
        if task_type == 'music':
            self.tasks.append({'type' : 'music', 'ytid' : ytid, 'messageId' : messageId, 'userId' : userId})
            return True
            
        elif task_type == 'video':
            self.tasks.append({'type' : 'video', 'ytid' : ytid, 'resolution' : resolution, 'messageId' : messageId, 'userId' : userId})
            return True
    
    async def getTask(self) -> dict:
        if len(self.tasks) >= 1:
            return self.tasks.pop(0)
        
        
    async def addFinishedTask(self, task_type : str = 'type', ytid : str = None, resolution : str = '144p', finished : bool = True, dataId : int = None, messageId : int = None, userId : int = None) -> bool:
        if task_type == 'music':
            self.finished_tasks.append({'type' : 'music', 'ytid' : ytid, 'finished' : finished, 'dataId' : dataId, 'messageId' : messageId, 'userId' : userId})
            return True
            
        elif task_type == 'video':
            self.finished_tasks.append({'type' : 'video', 'ytid' : ytid, 'resolution' : resolution, 'finished' : finished, 'dataId' : dataId, 'messageId' : messageId, 'userId' : userId})
            return True
    
    async def getFinishedTask(self) -> dict:
        if len(self.finished_tasks) >= 1:
            return self.finished_tasks.pop(0)