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


	def creat_user_table(self, table_name):
		self.user_table = table_name
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ('user_name', 'user_id', 'action', 'lang');")

		conection.commit()
		conection.close()

	def show_user_table(self):
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		for row in cursor.execute(f"SELECT * FROM {self.user_table};"):
			print(row)

		conection.commit()
		conection.close()

	def available_user(self, update):
		respons = False
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()

		for row in cursor.execute(f"SELECT * FROM {self.user_table};"):
			if row[1] == update.message.chat.id:
				respons = True
				break

		conection.commit()
		conection.close()
		return respons

	def add_user(self, update, username = "User"):
		user_id = update.message.chat.id
		user_data = [username, user_id,"def", "uz"]

		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		cursor.execute(f"INSERT INTO {self.user_table} VALUES (?, ?, ?, ?);", user_data)

		conection.commit()
		conection.close()
		print(f"{username} datbasega qo'shildi.")


	def get_user_action(self, user_id):
		respons = False
		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		for row in cursor.execute(f"SELECT * FROM {self.user_table};"):
			if row[1] == user_id:
				respons = row[2]
				break

		conection.commit()
		conection.close()
		return respons

	def set_user_action(self, user_id, action):
		# print(f"user id: {user_id}")
		# print(f"lang: {lang}")

		conection = sqlite3.connect(self.file_name)
		cursor = conection.cursor()
		cursor.execute(f"UPDATE {self.user_table} SET action = '{action}' WHERE user_id == {user_id};")

		conection.commit()
		conection.close()
	


if __name__ == '__main__':
	database = Bot_database("test.db")

	database.creat_user_table("users")
	# database.show_user_table()


