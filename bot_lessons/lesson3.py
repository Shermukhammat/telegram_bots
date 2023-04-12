from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton, BotCommand, InputMediaPhoto
from random import randint

ADMIN_ID = 1661189380
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'

buttons = [
	[InlineKeyboardButton(text = "Send photo", callback_data = 'send_photo'), 
	InlineKeyboardButton(text = "Send Documen", callback_data = "send_document"),
	InlineKeyboardButton(text = "Change photo", callback_data = "change_photo")],

	[InlineKeyboardButton(text = "Send media group", callback_data = "sen_media")]]


def start_command(update, context):
	update.message.reply_photo(
		photo = open('photos/hello_bot.png', 'rb'),
		# photo = 'https://picsum.photos/400/200',
		caption = f"Salom {update.message.chat.first_name} !",
		reply_markup = InlineKeyboardMarkup(buttons))

def text_fun(update, context):
	# context.user_data -> Xarbir Foydalanuvchi uchun aloxida dict

	if context.user_data.get('message'):
		words = context.user_data['message']
	else:
		words = []
	words.append(update.message.text)
	context.user_data['message'] = words

	print(f"{update.message.from_user.username} : {words}")

def inlen_core(update, context):
	query = update.callback_query

	if query.data == "send_document":
		query.message.reply_document(
			document = open('lesson1.py'),
			caption = '1-darsda yozilgan botning ko\'di :)',
			reply_markup = InlineKeyboardMarkup(buttons))

	elif query.data == 'send_photo':
		query.message.reply_photo(
			photo = f'https://picsum.photos/id/{randint(10, 100)}/400/200',
			caption = 'Rasim Jo\'natildi!',
			reply_markup = InlineKeyboardMarkup(buttons))

	elif query.data == "change_photo":
		query.message.edit_media(media = InputMediaPhoto(media = f'https://picsum.photos/id/{randint(10, 100)}/400/200'))
		query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons))

	elif query.data == "sen_media":
		query.message.reply_media_group(
			media = [InputMediaPhoto(media = open('photos/girl.jpg', 'rb')),
			
			InputMediaPhoto(media = f'https://picsum.photos/id/{randint(10, 100)}/400/200'),
			InputMediaPhoto(media = f'https://picsum.photos/id/{randint(10, 100)}/400/200')
			])

def photo_handler(update, context):
	file = update.message.photo[-1].file_id
	obj = context.bot.get_file(file)
	obj.download('photos/user_photo.jpg')

def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', start_command))
	dispatcher.add_handler(MessageHandler(Filters.text, text_fun))
	dispatcher.add_handler(CallbackQueryHandler(inlen_core))

	dispatcher.add_handler(MessageHandler(Filters.photo, photo_handler))

	updater.start_polling()
	updater.idle()


if __name__ == '__main__':
	main()