from loader import app, db


# Adding Tasks
@app.get("/addMusicTask")
async def addMusicTask(ytid : str = None, messageId : int = None, userId : int = None):
    if await db.addTask(task_type = 'music', ytid = ytid, messageId = messageId, userId = userId):
        return {"status" : 1}
    return {"status" : 0}


@app.get("/addVideoTask")
async def addVideoTask(ytid : str = None, resolution : str = '144p', messageId : int = None, userId : int = None):
    if await db.addTask(task_type = 'video', ytid = ytid, resolution = resolution, messageId = messageId, userId = userId):
        return {"status" : 1}
    return {"status" : 0}



# Adding Finished Tasks
@app.get("/addFinishedMusicTask")
async def addFinishedMusicTask(ytid : str = None, finished : bool = False, dataId : int = None, messageId : int = None, userId : int = None):
    if await db.addFinishedTask(task_type = 'music', ytid = ytid, finished = finished, dataId = dataId, messageId = messageId, userId = userId):
        return {"status" : 1}
    return {"status" : 0}


@app.get("/addFinishedVideoTask")
async def addFinishedVideoTask(ytid : str = None, resolution : str = '144p', finished : bool = False, dataId : int = None, messageId : int = None, userId : int = None):
    if await db.addFinishedTask(task_type = 'video', ytid = ytid, resolution  = resolution, finished = finished, dataId = dataId, messageId = messageId, userId = userId):
        return {"status" : 1}
    return {"status" : 0}
