import sqlite3


class Database:
    def __init__(self, file_path : str = "data/data.db") -> None:
        self.path = file_path
        
        self.conection = sqlite3.connect(file_path)
        self.cursor = self.conection.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS users (INT 'id', TEXT 'name', TEXT 'registred');")
        

        self.conection.commit()
        