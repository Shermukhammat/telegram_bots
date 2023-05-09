from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

API_TOKEN = "6080581500:AAHnIOY5m2wjqjE_uQUDMFAvLBC0L97eo20"
CHANEL_ID = '-1001942672781'

def start_function(update, context):
    user_name = update.message.chat.first_name
    update.message.reply_text(f"Salom {user_name}!")
    # print(update.message)

def core_function(update, context):
    pass


def video_handler(update, context):
    # print(update)
    print(update.message.caption)
    # print(update.message.video.caption)


def main():
    updater = Updater(token = API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start_function))

    dispatcher.add_handler(MessageHandler(Filters.text, core_function))

    dispatcher.add_handler(MessageHandler(Filters.video, video_handler))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("Starting bot ...")
    main()