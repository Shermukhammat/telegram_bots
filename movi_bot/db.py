import sqlite3


class Database:
    def __init__(self, file_name):
        self.name = file_name

    def conect(self, movies_tb = 'movies_data', user_tb = 'users_data'):
        self.movies = movies_tb
        self.users = user_tb

        conection = sqlite3.connect(self.name)
        cursor = conection.cursor()
        
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.movies} ('message_id' INTEGER, 'file_id' INTEGER, 'caption', 'file_size' INTEGER);")
        cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.users} ('user_id' INTEGER, 'user_name');")

        conection.commit()
        conection.close()
        print(f"database sucsesfuly conected...")


if __name__ == '__main__':
    database = Database('database.db')
    database.conect()