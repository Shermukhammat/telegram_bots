from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton
from googletrans import Translator

translator = Translator()
defolt_lang = "en"

def star(update, context):
	buttons = [[KeyboardButton(text = "uzn-en mode 🇺🇿-🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿-🇷🇺")]]
	user = update.message.chat.first_name

	update.message.reply_text(
		text = f"Assalomu alykum {user} xush kelibsiz!\nMen TarjimonRobotman!",
		reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

def translatorf(message, en_ru):
	lang = translator.detect(message).lang
	if lang == en_ru:
		return translator.translate(message, "uz").text
	elif lang == 'uz':
		return  translator.translate(message, en_ru).text
	else:
		return "Afsuz bu so'zni tarjima qila olmadim :("


def auto_translator(update, context):
	print(update)
	global defolt_lang 
	message = update.message.text
	if message == "uzn-en mode 🇺🇿-🇬🇧":
		defolt_lang = "en"
		update.message.reply_text("O'zbekcha Inglizcha tartibi yoqildi")
	elif message == "uzb-ru mode 🇺🇿-🇷🇺":
		defolt_lang = 'ru'
		update.message.reply_text("O'zbekcha Ruscha tartibi yoqildi")
	else:
		respons = translatorf(message, defolt_lang)
		if respons != message:
			update.message.reply_text(respons)
		else:
			update.message.reply_text("Afsuz bu so'zni tarjima qila olmadim :(")

	# print(lang)

def main():
	updater = Updater(token = '6082856375:AAEfdW4af8iJE6JBjHC_wStDWAt_GJWkzrQ')
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', star))
	dispatcher.add_handler(MessageHandler(Filters.text, auto_translator))

	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	main()