from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, BotCommand

ADMIN_ID = 1661189380
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'

def start_command(update, context):
	commands =[
	BotCommand(command = "start", description = "Botni ishga tushurish"),
	BotCommand(command = "restart", description = "Botni qayat ishga tushurish"),
	BotCommand(command = "menu", description = "Menuni chiqarish"),
	BotCommand(command = "info", description = "Bot haqida ma'lumot olish"),
	BotCommand(command = "settings", description = "sozlamalarni chiqarish2")]

	context.bot.set_my_commands(commands = commands)
	buttons = [[InlineKeyboardButton(text = "IT", callback_data = "it"), InlineKeyboardButton(text = "SMM", callback_data = "smm")]]
	update.message.reply_text(text=f"<b>Assalomu alaykum</b> <i>{update.message.chat.first_name}</i>",
		parse_mode = "HTML",
		reply_markup = InlineKeyboardMarkup(buttons))

def inlen_core(update, context):
	message = update.callback_query.message.text
	data = update.callback_query.data

	if data == 'it' or data == 'it_menu':
		buttons = [[InlineKeyboardButton(text = "Backend", callback_data = "backend"), InlineKeyboardButton(text = "Frontend", callback_data = "frontend")],
		[InlineKeyboardButton(text = "Disine", callback_data = 'dis'), InlineKeyboardButton(text = "AI", callback_data = "ai")],
		[InlineKeyboardButton(text = "back", callback_data = "bosh_menu")]]

		update.callback_query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons))
	
	elif data == "backend":
		buttons = [
			[InlineKeyboardButton(text = "Python", callback_data = "py"), InlineKeyboardButton(text = "Java", callback_data = "ja")],
			[InlineKeyboardButton(text = "sqlite3", callback_data = "sql"), InlineKeyboardButton(text = "Rubiy", callback_data = "rb")],
			[InlineKeyboardButton(text = "back", callback_data = "it_menu")]
		]

		update.callback_query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons))

	elif data == 'bosh_menu':
		buttons = [[InlineKeyboardButton(text = "IT", callback_data = "it"), InlineKeyboardButton(text = "SMM", callback_data = "smm")]]

		update.callback_query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons))

	elif data == 'py':
		update.callback_query.message.reply_text("Python yaxshi dasturlash tili !")


def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start_command))
	dispatcher.add_handler(CallbackQueryHandler(inlen_core))



	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()