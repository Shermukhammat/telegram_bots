from loader import app
import handlers, uvicorn



if __name__ == '__main__':
    uvicorn.run("app:app", host="127.1.1.1", port=7070)