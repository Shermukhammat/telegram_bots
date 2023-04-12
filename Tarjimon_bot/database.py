import sqlite3
import os

def columns_join(columns):
	respons = ""
	for n in range(len(columns)):
		if n != len(columns)-1:
			respons += f"'{columns[n]}',"
		else:
			respons += f"'{columns[n]}'"
	return respons

def make_question(column):
    respons = ""
    leng = len(column)
    for n in range(leng-1):
        respons+="?, "
    return respons+"?"

class Bot_database:
	def __init__(self, db_file_name):
		self.file_name = db_file_name


	def creat_tables(self, user_table_name = "users", chat_listb_name = "chat_list", cheet_tb_name = "cheet"):
		self.user_table = user_table_name
		self.chat_list = chat_listb_name
		self.cheet_tb = cheet_tb_name

		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		cursor.execute(f"CREATE TABLE IF NOT EXISTS {user_table_name} ('user_id' INTEGER PRIMARY KEY, 'user_name', 'lang', 'action', 'where');")
		cursor.execute(f"CREATE TABLE IF NOT EXISTS {chat_listb_name} ('user_id' INTEGER PRIMARY KEY, 'conversation' json);")

		cursor.execute(f"CREATE TABLE IF NOT EXISTS {cheet_tb_name} ('user_id' INTEGER PRIMARY KEY, 'message');")

		conection.commit()
		conection.close()


	def available_user(self, user_id):
		"""
		This function can chack user

		parms:
			user_id : int;
		"""
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		cursor.execute(f"SELECT user_id FROM {self.user_table} WHERE user_id == '{user_id}';")
		respons = cursor.fetchall()

		conection.commit()
		conection.close()
		if len(respons) > 0:
			if respons[0][0] == user_id:
				return True
			else:
				return False
		else:
			return False

	def add_user(self, user_id, user_name, lang):
		"""
		This function can add user;
		params:
			user_id : int (unicalni);
			user_name : str;
			lang : str (uz/ru/en);
		"""
		dic = {'new_mesage' : 0, 'messages' : []}
  
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		cursor.execute(f"INSERT INTO {self.user_table} VALUES (?, ?, ?, ?, ?);", (user_id, user_name, lang, 'nofing', 'head_menu'))
		cursor.execute(f"INSERT INTO {self.chat_list} VALUES (?, ?);", (user_id, f"{dic}"))
		# cursor.execute(f"INSERT INTO {self.cheet_tb} VALUES (?, ?, ?, ?, ?);", (user_id, user_name, lang, 'nofing', 'head_menu'))
		
		conection.commit()
		conection.close()
		print(f"{user_name} datbasega qo'shildi.")

	def get_user_data(self, user_id, chat = False):
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		if chat == False:
			cursor.execute(f"SELECT *  FROM {self.user_table} WHERE user_id == '{user_id}';")
			user_data = cursor.fetchall()
		
			conection.commit()
			conection.close()

			if len(user_data) == 1:
				return {'user_data' : user_data[0]}
		else:
			cursor.execute(f"SELECT *  FROM {self.user_table} WHERE user_id == '{user_id}';")
			user_data = cursor.fetchall()

			cursor.execute(f"SELECT *  FROM {self.chat_list} WHERE user_id == '{user_id}';")
			chat = cursor.fetchall()

			conection.commit()
			conection.close()
			
			if len(user_data) == 1 and len(chat) == 1:
				return {'user_data' : user_data[0], 'chat' : chat[0]}

	def updata_user_data(self, user_id, chat = False):
		pass


if __name__ == '__main__':
	database = Bot_database("test.db")

	database.creat_tables(user_table_name = "users_data", chat_listb_name = "chat", cheet_tb_name = "cheet")
	# print(database.available_user(101))
	# database.add_user('01111', 'SHermuxammad', 'uz')
	data = database.get_user_data('1111', chat = False)
	print(data)
	




