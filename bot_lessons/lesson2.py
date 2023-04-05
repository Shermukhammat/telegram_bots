from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, KeyboardButton, ChatAction

ADMIN_ID = 1661189380

def start_command(update, context):
	update.message.reply_text(text="Assalom alaykum!")

def show_menu(update, context):
	buttons = [
		[KeyboardButton(text="🔵 Contact", request_contact=True), KeyboardButton(text = "🟢 Location", request_location=True)],
		[KeyboardButton(text = "coming sonn3..."), KeyboardButton(text = "coming4 sonn...")] ]

	update.message.reply_text(
		text="Menu",
		reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True))


def tex_handler(update, context):
	message = update.message.text
	print(f"\nOUTPUT: {message}")
	respons = input(">>>")
	update.message.reply_text(text = f"{respons}")


def catch_contact(update, context):
	phone_number = update.message.contact.phone_number
	print(f"Yangi foydalanuvchi : {phone_number} qo'shildi!")
	context.bot.send_message(chat_id = ADMIN_ID, text = f"Yangi foydalanuvchi {phone_number}!")
	# update.message.reply_text(text = f"Sizning raqamingiz ro'yxatga olindi")

def catch_location(update, context):
	location = update.message.location
	context.bot.send_location(chat_id = ADMIN_ID, latitude = location.latitude, longitude = location.longitude)
	update.message.reply_text("lakatsiyangiz adminga yuborildi!")
	print("New location:")
	print(location.latitude)
	print(location.longitude)



def main():
	updater = Updater(token = '6082856375:AAEfdW4af8iJE6JBjHC_wStDWAt_GJWkzrQ')
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start_command))
	dispatcher.add_handler(CommandHandler('menu', show_menu))
	dispatcher.add_handler(MessageHandler(Filters.text, tex_handler))
	dispatcher.add_handler(MessageHandler(Filters.contact, catch_contact))
	dispatcher.add_handler(MessageHandler(Filters.location, catch_location))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()