from telegram import KeyboardButton, BotCommand, InlineKeyboardButton

CONTEXT = {'you_chose_lang': 
			{
			'uz' : 'Siz o\'zbek tilini tanladingiz !',
			'en' : 'You have selected English !',
			'ru' : 'Вы выбрали русский язык !'
			},

		'hello_my_name' : 
			{
			'uz' : 'Assalomu alykum Men TarjimonRobotman!',
			'ru' : 'Здравствуйте, я TarjimonRobot!',
			'en' : "Hello, I'm TranslatorRobot!"
			},

		'which_lang' : 
			{
			'uz' : 'Qaysi til sizga qulay?',
			'en' : 'Which language is the best for you?',
			'ru' : 'Какой язык вам удобен?'
			},
		'need_sign_up' : 
			{
				'uz' : "Afsus siz ro'yxatdan o'tmagansiz! Iltimos, ro'yxatdan o'tish uchun ismigizni Jo'nating",
				'en' : "Sorry you are not registered! Please, Send your name to register",
				'ru' : "Извините, вы не зарегистрированы! Пожалуйста, укажите свое имя, чтобы зарегистрироваться"
			},
		'well_name' : 
			{
				'uz' : ["Yaxshi ", "! Agar ismingizni xato kiritgan bo'lsangiz qaytadan ismingizni jo'natishingiz mumkun!"],
				'en' : ["Good ", "! If you entered your name incorrectly, you may send your name again!"],
				'ru' : ["Добрый",  " ! Если вы ввели свое имя неправильно, вы можете отправить свое имя еще раз!"]
			},
		'your_name' : 
			{
				'uz' : ["Sizning ismingiz ", "ga o'zgartirildi!"],
				'en' : ["Your name has been changed to ", "!"],
				'ru' : ["Ваше имя изменено на ", "!"]
			},
		'head_menu' : {'uz' : 'Bosh menu', 'ru' : 'Главное меню', 'en' : 'Head menu'}
		}

class Message_media:
	def __init__(self):
		pass

	def get_inline_lang(self, lang = 'uz'):
		settings = {
			'uz' : {
				"🇺🇿 o'zbekcha" : "set_uz", 
				"🇷🇺 Ruscha" : 'set_ru', 
				"🇬🇧 Inglizcha" : 'set_en'},
			'ru' : {
				"🇺🇿 узбекский" : "set_uz", 
				"🇷🇺 Русский" : 'set_ru', 
				"🇬🇧 Английский" : 'set_en'},
			'en' : {
				"🇺🇿 Uzbek" : "set_uz", 
				"🇷🇺 Russian" : 'set_ru', 
				"🇬🇧 English" : 'set_en'}
			}

		inline_buttons = []
		for message, data in settings[lang].items():
			inline_buttons.append(InlineKeyboardButton(text = message, callback_data = data))

		return inline_buttons

	def get_regist_button(self, lang = 'uz'):
		params = {
			'uz' : [KeyboardButton(text = "📝 Ro'yxatdan o'tish")],
			'ru' : [KeyboardButton(text = '📝 Зарегистрироваться')],
			'en' : [KeyboardButton(text = "📝 Sign up")]
			}
		return params[lang]

	def get_change_lang_inline(self, lang = 'uz'):
		params = {
			'uz' : "♻️ Tilni o'zgartirish",
			'en' : "♻️ Change the language",
			'ru' : "♻️ Изменить язык"
			}
		return [InlineKeyboardButton(text = params[lang], callback_data = "nouser_change_lang")]

	def get_uh_menu(self, lang = 'uz'):
		"""
			User head menu buttons
		"""
		params = {
			'uz' : [
				[KeyboardButton(text = "uzb-en mode 🇺🇿🔄🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Oxford Definition")],
				[KeyboardButton(text = "Aloqa 📲"), KeyboardButton(text = "⚙️ Sozlamalar")]],
			'ru' : [
				[KeyboardButton(text = "узб-анг мод 🇺🇿🔄🇬🇧"), KeyboardButton(text = "узб-ру мод 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Оксфорд дефинитион")],
				[KeyboardButton(text = "контакт 📲"), KeyboardButton(text = "⚙️ настройки")]],
			'en' : [
				[KeyboardButton(text = "uzb-en mode 🇺🇿🔄🇬🇧"), KeyboardButton(text = "uzb-ru mode 🇺🇿🔄🇷🇺"), KeyboardButton(text = "🛡 Oxford Definition")],
				[KeyboardButton(text = "Contact 📲"), KeyboardButton(text = "⚙️ Settings")]]}

		return params[lang]
if __name__ == '__main__':
	media = Media()
	print(media.get_inline_regist(lang = 'uz'))