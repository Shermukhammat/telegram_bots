from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton, BotCommand, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from database import Bot_database
from media import Message_media, CONTEXT
from  translator import translator
from test import RAM
from oxford import getDefination

"""
v.3.0.0
"""
def add_user(user_id, lang):
	if RAM_dic.get(user_id):
		RAM_dic[user_id]['lang'] = lang
		RAM_dic[user_id]['edit_count'] += 1
	else:
		RAM_dic[user_id] = {'lang' : lang, 'edit_count' : 0, 'send_name' : 0, 'user_name' : "0"}
API_TOKEN = '6082856375:AAH8nuCVOpIRRnVkaHyXdaSM9TzLiwjlKh0'

RAM_lis = []
RAM_dic = {}
RAM_admes = {}



def capital_letter(word):
	word = word.capitalize()
	if len(word) > 3:
		if word[1] == 'h':
			return word[0] + 'H' + word[2:]
	return word




ram = RAM()
database = Bot_database("test.db")
database.creat_tables(user_table_name = "users_data", chat_listb_name = "chat", cheet_tb_name = "cheet")

message_media = Message_media()
defolt_lang = "en"


def star(update, context):
	user_id = update.message.chat.id
	if database.available_user(user_id):
		user_data = database.get_user_data(user_id = user_id)
		name = user_data["user_data"]["name"]
		lang = user_data["user_data"]["lang"]

		message = CONTEXT["you_touch_start"][lang][0] + name + CONTEXT["you_touch_start"][lang][1]
		# print(type(message))
		update.message.reply_photo(photo = open('photos/hello_bot.png', 'rb'), caption = message)


		buttons = message_media.get_uh_menu(lang = lang)
		head_menu = CONTEXT['head_menu'][lang]

		update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

		# updating user data
		user_data["user_data"]['where'] = "head_menu"
		user_data["user_data"]['action'] = "nofing"
		database.update_user_data(user_data)

	else:
		if RAM_dic.get(user_id):
			lang = RAM_dic[user_id]['lang']
			update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = CONTEXT['which_lang'][lang],
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = lang)]))

		else:
			RAM_lis.append(user_id)
			update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = f"🇺🇿 Sizga qaysi til qulay?\n🇬🇧 Which language is the best for you?\n🇷🇺 Какой язык вам удобен?",
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = 'en')]))





def core_function(update, context):
	user_id = update.message.chat.id
	message = update.message.text
	# print(RAM_lis)
	buttons = ["uzb-en mode 🇺🇿🔄🇬🇧", "uzb-ru mode 🇺🇿🔄🇷🇺", "🛡 Oxford Definition", "Aloqa 📲", "⚙️ Sozlamalar"]
	
	# If user hase registered
	if database.available_user(user_id):
		user_data = database.get_user_data(user_id = user_id)
		name = user_data["user_data"]["name"]
		lang = user_data["user_data"]["lang"]
		where = user_data["user_data"]['where']
		action = user_data["user_data"]["action"]

		#HEAD MENU
		if where == "head_menu":
			# message = CONTEXT['uzen-mode'][lang]
   
			#Uzn -> eng menu
			if message in ["uzb-en mode 🇺🇿🔄🇬🇧", "узб-анг мод 🇺🇿🔄🇬🇧"]:
				
				buttons = message_media.get_translater_buttons(lang = lang, mode = "uz-en/en-uz")
				update.message.reply_text(text = CONTEXT["uz-en_menu"][lang], reply_markup  = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
				
				# updating user data
				user_data["user_data"]['where'] = "uzent_menu"
				database.update_user_data(user_data)
			
			# uz_rut_menu ->
			elif message in ["uzb-ru mode 🇺🇿🔄🇷🇺", "узб-ру мод 🇺🇿🔄🇷🇺"]:	
				buttons = message_media.get_translater_buttons(lang = lang, mode = "uz-ru/ru-uz")
				update.message.reply_text(text = CONTEXT["uz-ru_menu"][lang], reply_markup  = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
				
				# updating user data
				user_data["user_data"]['where'] = "uzrut_menu"
				database.update_user_data(user_data)

			elif message in ["🛡 Oxford Definition", "🛡 Оксфорд дефинитион"]:
				buttons = message_media.get_oxfor_menu(lang = lang)
				update.message.reply_text(text = CONTEXT['oxfor_menu'][lang], reply_markup  = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
    
    			# update user data
				user_data["user_data"]['where'] = "oxfor_menu"
				database.update_user_data(user_data)

			elif message in ["Aloqa 📲", "контакт 📲", "Contact 📲"]:
				buttons = message_media.get_contact_menu(lang = lang)

				update.message.reply_text(text = CONTEXT['contact_menu'][lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
				
				# update user data
				user_data["user_data"]['where'] = "contact_menu"
				database.update_user_data(user_data)


			elif message in ["⚙️ Sozlamalar", "⚙️ настройки", "⚙️ Settings"]:
				buttons = message_media.get_setingm(lang = lang)
				# print(buttons)
				update.message.reply_text(text = CONTEXT['settings'][lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# update user data
				user_data["user_data"]['where'] = 'settings'
				database.update_user_data(user_data)


			elif message in ["📈 statistika", "📈 статистика", "📈 statistics"]:
				update.message.reply_text("Building ...")

			elif message in ["🤖📂 malumot", "🤖📂 информация", "🤖📂 info"]:
				update.message.reply_text("Building ...")

		# UZ->ENG  MENU
		elif where == "uzent_menu":
			if message in ["🇺🇿 O'zbekchadan ➡️ 🇬🇧 Inglizchaga", "🇺🇿 from Uzbek to ➡️ 🇬🇧 English", "🇺🇿 from Uzbek to ➡️ 🇬🇧 English"]:
				update.message.reply_text(text = CONTEXT["uzen-mode"][lang])
    
				user_data["user_data"]["action"] = "uz-en"
				database.update_user_data(user_data)

			elif message in ["🇬🇧 Inglizchadan ➡️ 🇺🇿 O'zbekchaga", "🇬🇧 английского на ➡️ 🇺🇿 узбекский", "🇬🇧 From English to ➡️ 🇺🇿 Uzbek"]:
				update.message.reply_text(text = CONTEXT["enuz-mode"][lang])
    
				user_data["user_data"]["action"] = "en-uz"
				database.update_user_data(user_data)

			elif message in ["📑 qo'lanma", "📑 руководство", "📑  manual"]:
				update.message.reply_text("Coming soon...")
		
			# back to head menu
			elif message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				database.update_user_data(user_data)

			elif action == "uz-en":
				update.message.reply_text(translator(message, lang1 = 'uz', lang2 = 'en'))
			
			elif action == "en-uz":
				update.message.reply_text(translator(message, lang1 = 'en', lang2 = 'uz'))

		# UZ->RU MENU
		elif where == "uzrut_menu":
			if message in ["🇺🇿 O'zbekchadan ➡️ 🇷🇺 Ruschaga", "Из 🇺🇿 узбекского в ➡️ 🇷🇺 русского", "From 🇺🇿 Uzbek to ➡️ 🇷🇺 Russian"]:
				update.message.reply_text(text = CONTEXT["uzru-mode"][lang])
    
				user_data["user_data"]["action"] = "uz-ru"
				database.update_user_data(user_data)

			elif message in ["🇷🇺 Ruschadan ➡️ 🇺🇿 O'zbekchaga", "С 🇷🇺 русского на ➡️ 🇺🇿 узбекский", "From 🇷🇺 Russian to ➡️ 🇺🇿 Uzbek"]:
				update.message.reply_text(text = CONTEXT["ruuz-mode"][lang])
    
				user_data["user_data"]["action"] = "ru-uz"
				database.update_user_data(user_data)

			elif message in ["📑 qo'lanma", "📑 руководство", "📑  manual"]:
				update.message.reply_text("Coming soon...")
		
			# back to head menu
			elif message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				database.update_user_data(user_data)

			elif action == "uz-ru":
				update.message.reply_text(translator(message, lang1 = 'uz', lang2 = 'ru'))
			
			elif action == "ru-uz":
				update.message.reply_text(translator(message, lang1 = 'ru', lang2 = 'uz'))
   		
   		# CONTACT MENU
		elif where == "contact_menu":
			if message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				database.update_user_data(user_data)

			elif message in ["👨🏻‍💻 dasturchi", "👨🏻‍💻 Программист", "👨🏻‍💻 Programmer"]:
				coder = {'uz' : "👨🏻‍💻 dasturchi", 'ru' : "👨🏻‍💻 Программист", 'en' : "👨🏻‍💻 Programmer"}
				update.message.reply_text(f"{coder[lang]}: @shermukhammad_temirov")

			elif message in ["👮🏻‍♂️ Admin bilan aloqa", "👮🏻‍♂️ Contact Admin", "👮🏻‍♂️Связаться с Админом"]:
				text = name + CONTEXT["contact_with_admin"][lang]
				buttons = message_media.admin_chatm(lang = lang)

				update.message.reply_text(text = CONTEXT['admin_contact'][lang])
				update.message.reply_photo(photo = open('photos/hello_bot.png', 'rb'), caption = text, reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				user_data["user_data"]['where'] = "chat_admin"
				database.update_user_data(user_data)

		# CHAT ADMIN
		elif where == "chat_admin":
			if message in ["⬅️ orqaga", "⬅️ назад", "⬅️ back"]:
				buttons = message_media.get_contact_menu(lang = lang)

				update.message.reply_text(text = CONTEXT['contact_menu'][lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
				
				# update user data
				user_data["user_data"]['where'] = "contact_menu"
				database.update_user_data(user_data)
				ram.clear_usmes(user_id = user_id)

			elif message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				database.update_user_data(user_data)
				ram.clear_usmes(user_id = user_id)

			# SEND MESSAGE
			elif message in ["🚀 xabarlarni yuborish", "🚀 send messages", "🚀 отправлять сообщения"]:
				messages = ram.get_user_message(user_id = user_id)
				if len(messages) != 0:
					chat = database.get_user_data(user_id = user_id, chat = True)
					new_messages = int(chat['chat']['new_messages'])
					new_messages += len(messages)
					chat['chat']['new_messages'] = str(new_messages)

					message_data = chat['chat']['messages']
					if len(message_data) == 1:
						messages_data = []

					message_data.append(name)
					for mes in messages:
						message_data.append(mes)
					chat['chat']['messages'] = message_data

					database.update_user_data(chat)
					ram.clear_usmes(user_id = user_id)

					update.message.reply_text("Sizning xabaringiz yuborildi. Tez orada Sizga admin javobb beradi!")

				else:
					update.message.reply_text("Iltimos birinchi xabar jo'nating")


			else:
				message_data = update.message
				message_id = message_data['message_id']
				buttons = message_media.delet_message(lang = lang)	

				ram.user_message(message, user_id = user_id)
				print(ram.get_user_message(user_id = user_id))

				# print(RAM_admes)
				context.bot.delete_message(chat_id = int(user_id), message_id = message_id)
				update.message.reply_text(text = message, reply_markup = InlineKeyboardMarkup(buttons))

		elif where == 'settings':
			if message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				user_data["user_data"]['action'] = "nofing"
				database.update_user_data(user_data) 

			elif message in ["♻️ Tilni o'zgartirish", "♻️ Change the language", "♻️ Изменить язык"] and action != "chose_lang":
				buttons = message_media.get_inlang(lang = lang)
				update.message.reply_photo(photo = open('photos/chose_lang.png', 'rb'), caption = CONTEXT['which_lang'][lang], reply_markup = InlineKeyboardMarkup(buttons))

				# update user data
				user_data["user_data"]['action'] = "chose_lang"
				database.update_user_data(user_data)

			elif message in ["👤 Ismni O'zgartirish", "👤 Изменить имя", "👤 Change Name"] and action != 'send_name':


				update.message.reply_photo(photo = open('photos/bot_find.png', 'rb'), caption = CONTEXT['shell_sen_name'][lang])
				user_data["user_data"]['action'] = "send_name"
				database.update_user_data(user_data)
			
			elif message in ["✅ Qo'lash", "✅ применять", '✅ Apply']:
				new_name = ram.get_name(user_id = user_id)

				if new_name != None:
					buttons = message_media.get_setingm(lang = lang)
					sen_message = CONTEXT['your_name_changed'][lang][0] + new_name + CONTEXT['your_name_changed'][lang][1]
					update.message.reply_text(sen_message)
					update.message.reply_text(text = CONTEXT['settings'][lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))


					user_data["user_data"]['where'] = 'settings'
					user_data["user_data"]['name'] = new_name
					user_data["user_data"]['action'] = 'nofing'
					database.update_user_data(user_data)

			elif message in ["❌ Bekor qilish", "❌ cancel", "❌ Отмена"]:
				buttons = message_media.get_setingm(lang = lang)
				# print(buttons)
				update.message.reply_text(text = CONTEXT['settings'][lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# update user data
				user_data["user_data"]['where'] = 'settings'
				user_data["user_data"]['action'] = 'nofing'
				database.update_user_data(user_data)

			elif message in ["🆚 Bo't versiyasi", "🆚 Бот версия", "🆚 Bot version"]:
				sen_message = CONTEXT['bot_version'][lang]

				update.message.reply_text(sen_message)

			elif action == "send_name":
				new_name = message
				sen_message = CONTEXT['your_name'][lang][0] + new_name + CONTEXT['your_name'][lang][1]
				ram.save_name(new_name, user_id = user_id)
				buttons = message_media.get_change_name_buttons(lang = lang)

				update.message.reply_text(sen_message, reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

		elif where == 'oxfor_menu':
			if message in ["🏠 Bosh sahifaga", "🏠 Back to Home", "🏠 На главную"]:
				buttons = message_media.get_uh_menu(lang = lang)
				head_menu = CONTEXT['head_menu'][lang]

				update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))

				# updating user data
				user_data["user_data"]['where'] = "head_menu"
				database.update_user_data(user_data)
    
			elif message in ["📑 qo'lanma", "📑 руководство", "📑  manual"]:
				update.message.reply_text("Coming soon...")

			else:
				update.message.reply_text(getDefination(message))


	else:
		#Registir user
		if message in ["📝 Ro'yxatdan o'tish", '📝 Зарегистрироваться', "📝 Sign up"] and RAM_dic.get(user_id):
			user_name = RAM_dic[user_id]['user_name']
			lang = RAM_dic[user_id]['lang']
			buttons = message_media.get_uh_menu(lang = lang)

			database.add_user(int(user_id), user_name, lang)
			head_menu, you_hav_registr = CONTEXT['head_menu'][lang], CONTEXT['you_have_registred'][lang]

			update.message.reply_text(text = you_hav_registr)
			update.message.reply_text(text = head_menu, reply_markup =  ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))
			
		#Ask user name
		elif user_id in RAM_lis:
			if RAM_dic.get(user_id):
				# If user fir send your name
				lang = RAM_dic[user_id]['lang']

				if RAM_dic[user_id]['send_name'] == 0: 
					RAM_dic[user_id]['send_name'] =+ 1
					RAM_dic[user_id]['user_name'] = message
					buttons = message_media.get_regist_button(lang = lang)

					caption = f"{CONTEXT['well_name'][lang][0]} {message} {CONTEXT['well_name'][lang][1]}" # Well name ...
					
					update.message.reply_photo(photo = open('photos/happy_bot.png', 'rb'), 
						caption = caption,
						reply_markup = ReplyKeyboardMarkup([buttons], resize_keyboard = True, one_time_keyboard = True))
					
				
				else:
					# buttons = message_media.get_regist_button(lang = lang)
					RAM_dic[user_id]['user_name'] = message
					reply = CONTEXT['your_name'][lang][0] + message + CONTEXT['your_name'][lang][1] # Your name change ... 
					update.message.reply_text(reply)
				
			else:
				update.message.reply_photo(
				photo = open('photos/chose_lang.png', 'rb'),
				caption = f"🇺🇿 Sizga qaysi til qulay?\n🇬🇧 Which language is the best for you?\n🇷🇺 Какой язык вам удобен?",
				reply_markup = InlineKeyboardMarkup([message_media.get_inline_lang(lang = 'en')]))



def core_inline(update, context):
	user_id = update.callback_query.message.chat.id
	query = update.callback_query
	message_id = update.callback_query.message.message_id

	if database.available_user(user_id):
		data = update.callback_query.data
		message = update.callback_query.message.text

		user_data = database.get_user_data(user_id = user_id)
		name = user_data["user_data"]["name"]
		lang = user_data["user_data"]["lang"]
		where = user_data["user_data"]['where']
		action = user_data["user_data"]["action"]
		
		if where == "chat_admin":
			if data == "remove" :
				message_id = update.callback_query.message.message_id
				chat_id = update.callback_query.message.chat.id
				ram.delet_usmes(message, user_id = user_id)

				context.bot.delete_message(chat_id = chat_id, message_id = message_id)

		elif where == 'settings':
			print(data)
			if data in ["set_uz", 'set_ru', 'set_en']:
				new_lang = data[-2:]
				buttons = message_media.get_change_lang(lang = new_lang)
				ram.save_lang(new_lang, user_id = user_id)

				# query.message.edit_caption(f"siz tanladingiz")
				query.message.edit_media(media = InputMediaPhoto(caption = CONTEXT['you_chose_lang'][new_lang], media = open('photos/happy_bot.png', 'rb')), reply_markup = InlineKeyboardMarkup(buttons))
				# query.message.edit_caption("chnged!!")
				# query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup(buttons))
				# query.message.edit_caption(f"siz tanladingiz")
				# print(ram.get_lang(user_id = user_id))
			elif data == 'rechose':
				new_lang = ram.get_lang(user_id = user_id)
				buttons = message_media.get_inlang(lang = new_lang)

				query.message.edit_media(media = InputMediaPhoto(caption = CONTEXT['you_chose_lang'][lang], media = open('photos/chose_lang.png', 'rb')), reply_markup = InlineKeyboardMarkup(buttons))
			elif data == 'aply':
				new_lang = ram.get_lang(user_id = user_id)
				if new_lang != None:
					query.message.reply_text(CONTEXT['used_lang'][new_lang])

					# update user data
					user_data["user_data"]['lang'] = new_lang
					user_data["user_data"]['where'] = 'settings'
					database.update_user_data(user_data)

					#UPDATE SETINGS MENU
					buttons = message_media.get_setingm(lang = new_lang)
					query.message.reply_text(text = CONTEXT['settings'][new_lang], reply_markup = ReplyKeyboardMarkup(buttons, resize_keyboard = True, one_time_keyboard = True))


	elif user_id in RAM_lis:
		# print(query.data)
		if query.data in ["set_uz", "set_ru", "set_en"]:
			lang = query.data[-2:] #get lang
			add_user(user_id, lang)
			# RAM_dic[user_id] = {'lang' : lang}

			# context.bot.send_message(chat_id = user_id, text = CONTEXT['you_chose_lang'][lang])
			query.message.edit_media(media = InputMediaPhoto(media = open('photos/hello_bot.png', 'rb')))
			query.message.edit_caption(CONTEXT['you_chose_lang'][lang])
			buttons = message_media.get_change_lang_inline(lang = lang)
			query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup([buttons])) 

			if RAM_dic[user_id]['edit_count'] == 0:
				RAM_dic[user_id]['edit_count'] += 1
				query.message.reply_photo(
					photo = open('photos/upset_bot.png', 'rb'),
					caption = CONTEXT['need_sign_up'][lang])
		
		elif query.data == "nouser_change_lang":
			lang = RAM_dic[user_id]['lang']

			buttons = message_media.get_inline_lang(lang = lang)
			query.message.edit_reply_markup(reply_markup = InlineKeyboardMarkup([buttons]))



def main():
	updater = Updater(token = API_TOKEN)
	dispatcher = updater.dispatcher

	dispatcher.add_handler(CommandHandler('start', star))
	dispatcher.add_handler(MessageHandler(Filters.text, core_function))
	dispatcher.add_handler(CallbackQueryHandler(core_inline))

	updater.start_polling()
	updater.idle()


if __name__ == "__main__":
	print("starting bot... ")
	main()