from fastapi import FastAPI
from fastapi.responses import JSONResponse
from data import DataBase
from fastapi.responses import JSONResponse


async def not_found(request, exc):
    return JSONResponse(content={'status' : 0, 'detail': "Not found haha"}, status_code=exc.status_code)


exception_handlers = {404: not_found}
db = DataBase()
app = FastAPI(exception_handlers = exception_handlers)