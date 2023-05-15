from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import KeyboardButton, ReplyKeyboardMarkup

API_TOKEN = "6080581500:AAHnIOY5m2wjqjE_uQUDMFAvLBC0L97eo20"


def scrapper(update, context):
    chanel_data = context.bot.get_chat('@blahblat')
    print(chanel_data)
    CHANEL_ID = chanel_data['id']
    user_id = update.message.chat.id
    mesage_id = 21
    message_data = context.bot.copy_message(chat_id = user_id, from_chat_id = CHANEL_ID, message_id = 16)
    



def main():
    updater = Updater(token = API_TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('scrap', scrapper))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    print("Starting bot ...")
    main()