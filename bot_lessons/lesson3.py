from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, BotCommand

ADMIN_ID = 1661189380
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'

def start_command(update, context):
	global buttons
	buttons = [
	[InlineKeyboardButton(text = "Send photo", callback_data = 'send photo'), 
	InlineKeyboardButton(text = "Send Documen", callback_data = "send document"),
	InlineKeyboardButton(text = "Change photo", callback_data = "change photo")],

	[InlineKeyboardButton(text = "Send media group", callback_data = "send media")]
	]

	update.message.reply_photo(
		photo = open('photos/hello_bot.png', 'rb'),
		caption = f"Salom {update.message.chat.first_name} !",
		reply_markup = InlineKeyboardMarkup(buttons)
		)

def text_fun(update, context):
	pass

def inlen_core(update, context):
	pass


def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start_command))
	dispatcher.add_handler(MessageHandler(Filters.text, text_fun))
	dispatcher.add_handler(CallbackQueryHandler(inlen_core))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()