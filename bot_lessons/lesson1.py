from telegram.ext import Updater, CommandHandler, CommandHandler,


def start_command(update, context):
	# print("update message text: ", update.message.text)
	# print("context.bot : ", context.bot)
	# print("user id: ", update.message.from_user.id) #1661189380

	context.bot.send_message(chat_id = '1661189380', text='salom 2')
	# update.message.reply_text(text="Siz /start komandasni bosdingiz")

updater = Updater(token = '6082856375:AAEfdW4af8iJE6JBjHC_wStDWAt_GJWkzrQ')
dispatcher = updater.dispatcher

dispatcher.add_handler(CommandHandler('start', start_command))

updater.start_polling()
updater.idle()