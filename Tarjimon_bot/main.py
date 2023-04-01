from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, BotCommand
from googletrans import Translator
from database import Bot_database
"""
v.2.0.0
"""
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'
translator = Translator()
RAML = []

database = Bot_database("test.db")
database.creat_user_table("users")

defolt_lang = "en"

menu_buttons = [[KeyboardButton(text = "uzb-en mode 🇺🇿🔄🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Oxford Definition")],
	[KeyboardButton(text = "Aloqa 📲"), KeyboardButton(text = "⚙️ Sozlamalar")]]

def star(update, context):

	commands = [
		BotCommand(command = "start", description = "Botni ishga tushurish."),
		BotCommand(command = "restart", description = "Botni qayat ishga tushurish."),
		BotCommand(command = "info", description = "Bot statistikasni olish"),
		BotCommand(command = "help", description = "Botni ishlatish bo'ycha yordam")
		]

	update.message.reply_text(
		text = "Assalomu alykum xush kelibsiz!\nMen TarjimonRobotman!",
		reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard = True, one_time_keyboard = True))

def translatorf(message, en_ru):
	lang = translator.detect(message).lang
	if lang == en_ru:
		return translator.translate(message, "uz").text
	elif lang == 'uz':
		return  translator.translate(message, en_ru).text
	else:
		return "Afsuz bu so'zni tarjima qila olmadim :("

def lang_mode_hendler(update): 
	message = update.message.text
	if message == "uzn-en mode 🇺🇿-🇬🇧":
		# print("england")
		data_base.set_lang(update, 'en')
		update.message.reply_text("O'zbekcha Inglizcha tartibi yoqildi")
		return True
	elif message == "uzb-ru mode 🇺🇿-🇷🇺":
		# print("russia")
		data_base.set_lang(update, 'ru')
		update.message.reply_text("O'zbekcha Ruscha tartibi yoqildi")
		return True
	return False


def core_function(update, context):
	user_id = update.message.chat.id
	if database.available_user(update):
		message = update.message.text
		if message == "uzb-en mode 🇺🇿🔄🇬🇧":
			database.set_user_action(user_id, "en")
			update.message.reply_text("O'zbekch Inglizcha tartibi yoqildi.")
		elif message == "uzb-ru mode 🇺🇿🔄🇷🇺":
			database.set_user_action(user_id, "ru")
			update.message.reply_text("O'zbekch Ruscha tartibi yoqildi.")
		elif message == "🛡 Oxford Definition":
			database.set_user_action(user_id, "def")
			update.message.reply_text("Oxford Definition tartibi yoqildi.")
		elif message == "Aloqa 📲":
			buttons = [[KeyboardButton(text = "📬 SHikoyat va takliflar uchun"), KeyboardButton(text = "📌 Reklama berish")],
				[KeyboardButton(text = "⬅️ orqaga ")]]
			update.message.reply_text(text = "Aloqa bo'lmi:", reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

		elif message == "⬅️ orqaga":
			update.message.reply_text(text = "Bosh menu:", 
				reply_markup = ReplyKeyboardMarkup(menu_buttons, resize_keyboard = True, one_time_keyboard = True))


		# action = database.get_user_action(user_id)

		# update.message.reply_text(f"Your action is {action}.")

	else:
		if user_id not in RAML:
			update.message.reply_text("Siz ro'yxatdan o'tmagansiz! Iltimos ro'yxatdan o'tish uchun ismingzni kiriting!")
			RAML.append(user_id)
		else:
			username = update.message.text
			database.add_user(update, username = username)
			update.message.reply_text(f"{username} siz ro'yxatga olindingiz!")




def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', star))
	dispatcher.add_handler(MessageHandler(Filters.text, core_function))

	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()