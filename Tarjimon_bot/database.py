import sqlite3
import os
import json

def str_into_lis(string):
    respons = []
    for item in string[1:-2].split("\","):
        item = item.strip()
        respons.append(item[1:].replace('"', "'"))
    return respons

def lis_into_str(lis):
    str_array = "["
    for item in lis:
        str_array += f'"{item}", '
    
    return str_array[:-2]+"]"



def convertor(tuple):
    print(len(tuple) % 2)


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
		cursor.execute(f"CREATE TABLE IF NOT EXISTS {chat_listb_name} ('user_id' INTEGER PRIMARY KEY, 'new_messages', 'messages');")

		cursor.execute(f"CREATE TABLE IF NOT EXISTS {cheet_tb_name} ('user_id' INTEGER PRIMARY KEY,'messages');")

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
			user_id : int (unicalnidatabase);
			user_name : str;
			lang : str (uz/ru/en);
		"""
		dic = {"new_mesage" : "0", "messages" : " "}
  
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		cursor.execute(f"INSERT INTO {self.user_table} VALUES (?, ?, ?, ?, ?);", (user_id, user_name, lang, 'nofing', 'head_menu'))
		cursor.execute(f"INSERT INTO {self.chat_list} VALUES (?, ?, ?);", (user_id, '0', "[]"))
		# cursor.execute(f"INSERT INTO {self.cheet_tb} VALUES (?, ?, ?, ?, ?);", (user_id, user_name, lang, 'nofing', 'head_menu'))
		
		conection.commit()
		conection.close()
		print(f"{user_name} datbasega qo'shildi.")

	def get_user_data(self, user_id, chat = False):
		"""
		GET USER DAT 
		this function can get user data with user data;

		Args:
			user_id (int/str): find user data with id;
			chat (bool, optional): If chat to be True, return chat data. Defaults to False.

		Returns:
			dict: {'user_data' : {'user_id : int, 'name' : str, 'lang' : str, 'where' : str}, (if chat param == True) 'chat' : {'user_id' : int, 'messages' : JSON}'}
		"""
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		if chat == False:
			cursor.execute(f"SELECT *  FROM {self.user_table} WHERE user_id == '{user_id}';")
			user_data = cursor.fetchall()
		
			conection.commit()
			conection.close()

			if len(user_data) == 1:
				user_id, name, lang, action, where = user_data[0][0], user_data[0][1], user_data[0][2], user_data[0][3], user_data[0][4]
				return {'user_data' : {'user_id' : user_id, 'name' : name, 'lang' : lang, 'action' : action, 'where' : where}, 'chat' : None}
		else:
			cursor.execute(f"SELECT *  FROM {self.user_table} WHERE user_id == '{user_id}';")
			user_data = cursor.fetchall()

			cursor.execute(f"SELECT *  FROM {self.chat_list} WHERE user_id == '{user_id}';")
			chat = cursor.fetchall()

			conection.commit()
			conection.close()
			
			if len(user_data) == 1 and len(chat) == 1:
				user_id, name, lang, action, where = user_data[0][0], user_data[0][1], user_data[0][2], user_data[0][3], user_data[0][4]
				new_messages, messages = chat[0][1], chat[0][2]
				# messages = messages.replace("\'", "\"")
				# print(messages)
				# messages = json.loads(messages.replace('"', "'"))
				return {'user_data' : {'user_id' : user_id, 'name' : name, 'lang' : lang, 'action' : action ,'where' : where}, 'chat' : {'user_id' : user_id, 'new_messages' : new_messages, 'messages' : str_into_lis(messages)}}

	def update_user_data(self, user_data):
		"""_summary_

		Args:
			user_data (JSON): _description_
		"""

		if user_data["chat"] == None:
			conection = sqlite3.connect(self.file_name)
			cursor = conection.cursor()

			user = user_data['user_data']
			user_id, name, lang, action, where = user['user_id'], user['name'], user['lang'], user['action'], user['where']			
   
			cursor.execute(f"UPDATE {self.user_table} SET user_name = '{name}', lang = '{lang}', action = '{action}', 'where' = '{where}' WHERE user_id == {user_id};")
			# print(f"{self.user_table} table has sucsefuly updateded!")

		else:
			# print(user_data)
			conection = sqlite3.connect(self.file_name)
			cursor = conection.cursor()
			user = user_data['user_data']
			user_id, name, lang, action, where = user['user_id'], user['name'], user['lang'], user['action'], user['where']
			messages = lis_into_str(user_data["chat"]["messages"])
			messages = messages.replace("'", '"')
			new_messages = user_data["chat"]["new_messages"]
   
			cursor.execute(f"UPDATE {self.user_table} SET user_name = '{name}', lang = '{lang}', action = '{action}', 'where' = '{where}' WHERE user_id == {user_id};")
			cursor.execute(f"UPDATE {self.chat_list} SET new_messages = '{new_messages}', messages = '{messages}'   WHERE user_id == {user_id};")
			
			# print(f"{self.user_table} table has sucsefuly updateded!")
			# print(f"{self.chat_list} table has sucsefuly updated!")
			# print(f"UPDATE {self.chat_list} SET new_messages = '{new_messages}' messages = '{messages}'   WHERE user_id == {user_id};")
			


		conection.commit()
		conection.close()


if __name__ == '__main__':
	database = Bot_database("test.db")

	database.creat_tables(user_table_name = "users_data", chat_listb_name = "chat", cheet_tb_name = "cheet")
	# # print(database.available_user(101))
	# database.add_user(10, 'SHermuxammad', 'uz')
	data = database.get_user_data(10, chat = True)
	print(data)
	# ls = ["user", "salom", "qalesiz", "?", "admin", "yaxshiku", "O'zingizda nima gaplar?", "user", 'menham yaxshi!2']
	new_user_data = {'user_data': {'user_id': 10, 'name': 'SHER', 'lang': 'ru', 'action': 'uz-en', 'where': 'contact'}, 'chat': {'user_id': 10, 'new_messages': '20', 'messages': ["user", "salom", "qalesiz?", "o'zingzchi?"]}}
	database.update_user_data(new_user_data)

	# data = database.get_user_data(10, chat = True)
	# print(data)




