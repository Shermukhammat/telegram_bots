from loader import app, db


@app.get("/getTask")
async def getTask(ytid : str = None, resolution : str = '144p'):
    task = await db.getTask()
    if task:
        task['status'] = 1
        return task
    return {"status" : 0}


@app.get("/getFinishedTask")
async def getFinishedTask(ytid : str = None, resolution : str = '144p'):
    task = await db.getFinishedTask()
    if task:
        task['status'] = 1
        return task
    return {"status" : 0}