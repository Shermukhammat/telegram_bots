import sqlite3
from datetime import datetime
import pytz 


class DataBase:
    def __init__(self, path : str = "data/data.db") -> None:
        self.path = path
        
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users  (id INTEGER PRIMARY KEY, name, lang, registred);""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS admins  (id INTEGER PRIMARY KEY, name, lang, registred);""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY, url, '144', '240', '360', '480', '720', '1080', '1440', '2160', '4320');""")

        conection.commit()
        conection.close()

        # Creating temorary data
        self.users = self.get_users()
        self.admins = self.get_admins()
    

        
    

    def get_users(self) -> dict:
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        data =  {user[0] : {'name' : user[1], 'lang' : user[2], 'registred' : user[3]} for user in cursor.execute("SELECT * FROM users;")}

        conection.commit()
        conection.close()

        return data
    
    def get_admins(self) -> dict:
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        data =  {user[0] : {'name' : user[1], 'lang' : user[2], 'registred' : user[3]} for user in cursor.execute("SELECT * FROM admins;")}

        conection.commit()
        conection.close()

        return data
    
    def is_user(self, id : int) -> bool:
        return self.users.get(id) != None
    
    def is_admin(self, id : int) -> bool:
        return self.admins.get(id) != None
    
    def registir(self, id : int = None, name : str = None, admin : str = False, lang : str = None) -> None:
        name = name.replace("'", '`')
        registred = self.now()
        
        if admin and self.users.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            name = self.users[id]['name']
            cursor.execute(f"INSERT INTO admins (id, name, lang, registred) VALUES ({id}, '{name}', '{lang}', '{registred}');")
            cursor.execute(f"DELETE  FROM users WHERE id == {id};")

            del self.users[id]
            self.admins[id] = {'name' : name, 'lang' : lang, 'registred' : registred}
            print(f'New admin {name}')

            conection.commit()
            conection.close()

        elif not admin:
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            cursor.execute(f"INSERT INTO users (id, name, lang, registred) VALUES ({id}, '{name}', '{lang}', '{registred}');") 
            self.users[id] = {'name' : name, 'lang' : lang, 'registred' : registred} 
            print('New user ', name)

            conection.commit()
            conection.close()
        

    def remove(self, id : int = None, admin : bool = False) -> None:
        if admin and self.admins.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            cursor.execute(f"DELETE  FROM admins WHERE id == {id};")
            del self.admins[id]
            
            conection.commit()
            conection.close()

        elif not admin and self.users.get(id):
            conection = sqlite3.connect(self.path)
            cursor = conection.cursor()

            cursor.execute(f"DELETE FROM users WHERE id == {id};")
            del self.users[id]

            conection.commit()
            conection.close()

    def now(self, zone : str = 'Asia/Tashkent'):
        zone_tz = pytz.timezone(zone)
        zone_time = datetime.now(zone_tz)

        return zone_time.strftime(f"%d.%m.%Y %H:%M")

if __name__ == '__main__':
    db = DataBase()
    print(db.now())
    # db.registir(id=1, name="sher2", lang='ru', admin = False)
    
    # print(db.admins)
    # print(db.users)

    # db.remove(id = 1, admin = False)