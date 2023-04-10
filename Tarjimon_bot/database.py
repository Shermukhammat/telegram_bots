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
		cursor.execute(f"CREATE TABLE IF NOT EXISTS {chat_listb_name} ('user_id' INTEGER PRIMARY KEY, 'conversation', 'new_message');")

		cursor.execute(f"CREATE TABLE IF NOT EXISTS {cheet_tb_name} ('user_id' INTEGER PRIMARY KEY, 'message');")

		conection.commit()
		conection.close()


	# def creat_locate_table(self, table_name):
	# 	self.located_table = table_name
	# 	conection = sqlite3.connect(self.file_name)
	# 	cursor = conection.cursor()

	# 	cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ('user_id', 'user_name', 'lang');")

	# 	conection.commit()
	# 	conection.close()

	# def show_user_table(self):
	# 	conection = sqlite3.connect(self.file_name)
	# 	cursor = conection.cursor()

	# 	for row in cursor.execute(f"SELECT * FROM {self.user_table};"):
	# 		print(row)

	# 	conection.commit()
	# 	conection.close()

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
		# """
		# user_data = [int(user_id), user_name, lang, 'nofing', 'head_menu']

		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		cursor.execute(f"INSERT INTO {self.user_table} VALUES (?, ?, ?, ?, ?);", (user_id, user_name, lang, 'nofing', 'head_menu'))

		conection.commit()
		conection.close()
		print(f"{user_name} datbasega qo'shildi.")


	# def get_user_action(self, user_id):
	# 	respons = False
	# 	conection = sqlite3.connect(self.file_name)
	# 	cursor = conection.cursor()
	# 	for row in cursor.execute(f"SELECT * FROM {self.user_table};"):
	# 		if row[1] == user_id:
	# 			respons = row[2]
	# 			break

	# 	conection.commit()
	# 	conection.close()
	# 	return respons

	# def set_user_action(self, user_id, action):
	# 	# print(f"user id: {user_id}")
	# 	# print(f"lang: {lang}")

	# 	conection = sqlite3.connect(self.file_name)
	# 	cursor = conection.cursor()
	# 	cursor.execute(f"UPDATE {self.user_table} SET action = '{action}' WHERE user_id == {user_id};")

	# 	conection.commit()
	# 	conection.close()
	


if __name__ == '__main__':
	database = Bot_database("test.db")

	database.creat_tables()
	# print(database.available_user(101))
	database.add_user(1125, "SHermuhammad", 'uz')

	# database.show_user_table()


