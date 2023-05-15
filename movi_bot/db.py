import sqlite3


class Database:
    def __init__(self, file_name):
        self.name = file_name

    def conect(self, movies_tb = 'movies_data', user_tb = 'users_data'):
        self.movies = movies_tb
        self.users = user_tb

        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('message_id' INTEGER, 'file_id', 'caption', 'file_size' INTEGER);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('user_id' INTEGER, 'user_name');")

        conection.commit()
        conection.close()
        print(f"database sucsesfuly conected...")

    def add_movi(self, caption, message_id = None, size = 0, file_id = None):
        """
            caption : str
            message_id : int
            size : int
            file_id : str
        """
        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()

        cursor.execute(f"INSERT INTO {self.movies} VALUES (?, ?, ?, ?)", (message_id, file_id, caption, size))

        conection.commit()
        conection.close()
        print("New movi added")
        


if __name__ == '__main__':
    database = Database('database.db')
    database.conect()