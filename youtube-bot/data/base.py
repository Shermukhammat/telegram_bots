import sqlite3
from datetime import datetime
import pytz 
import json


class DataBase:
    def __init__(self, path : str = "data/data.db", settings_path : str = "data/data.json") -> None:
        self.path = path
        
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS users  (id INTEGER PRIMARY KEY, name, lang, registred);""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS admins  (id INTEGER PRIMARY KEY, name, lang, registred);""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS videos (id INTEGER PRIMARY KEY, youtube_id);""")
        cursor.execute("""CREATE TABLE IF NOT EXISTS resolutions (id INTEGER PRIMARY KEY, video_id INTEGER, resolution, itag INTEGER, lastModified INTEGER, size, telegram_id INTEGER);""")

        conection.commit()
        conection.close()

        # Creating temorary data
        self.users = self.get_users()
        self.admins = self.get_admins()
    

        self.settings_path = settings_path

        js = open(settings_path, 'r')
        self.data = json.loads(js.read())
        js.close()

    def update(self):
        js = open(self.file, 'w')
        js.write(json.dumps(self.data))
    

    def get_users(self) -> dict:
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        data =  {user[0] : {'name' : user[1], 'lang' : user[2], 'registred' : user[3], 'menu' : False} for user in cursor.execute("SELECT * FROM users;")}

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
    

    def update_user_lang(self, id : int = None, lang : str = None):
        conection = sqlite3.connect(self.path)
        cursor = conection.cursor()

        cursor.execute(f"UPDATE users SET lang = '{lang}' WHERE id == {id};")
        self.users[id]['lang'] = lang 

        conection.commit()
        conection.close()

    
    def get_user_info(self, id : int = None) -> str:
        user = self.users[id]
        if user['lang'] == 'uz':
            return f"👤 Foydalanuvchi: {user['name']}  \n⏳ Ro'yxatdan o'tdi: {user['registred']}"
        
        elif user['lang'] == 'ru':
            return f"👤 Пользователь: {user['name']}  \n⏳ Зарегистрирован: {user['registred']}"
        
        elif user['lang'] == 'en':
            return f"👤 User: {user['name']}  \n⏳ Registered: {user['registred']}"
        
    
    
if __name__ == '__main__':
    db = DataBase()
    print(db.now())
    # db.registir(id=1, name="sher2", lang='ru', admin = False)
    
    # print(db.admins)
    # print(db.users)

    # db.remove(id = 1, admin = False)