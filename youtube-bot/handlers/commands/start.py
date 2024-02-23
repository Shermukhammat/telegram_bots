from loader import dp, db, types, context, buttons, inline
from aiogram.dispatcher import FSMContext



@dp.message_handler(commands = 'start', state = "*")
async def start_message_handler(update : types.Message, state : FSMContext):
    if db.is_user(id = update.from_user.id):
        user = db.users[update.from_user.id]
        await update.answer(text = db.get_user_info(id = update.from_user.id),
                            reply_markup = buttons.head_menu(lang = user['lang']))
        
        current_state = await state.get_state()
        if current_state:
            await state.finish()

    
    elif db.is_admin(id  = update.from_user.id):
        await update.answer("You are admin")
        

    else:
        if update.from_user.language_code in ['uz', 'en', 'ru']:
            lang = update.from_user.language_code
        else:
            lang = 'en'
        
        db.registir(id = update.from_user.id, 
                    name = update.from_user.first_name, 
                    lang = lang)
        

        user = db.users[update.from_user.id]
        await update.answer(text = context.welcome_user(user), reply_markup = buttons.head_menu(lang = lang))
    


@dp.message_handler(commands = 'remove', state = "*")
async def debuger(update : types.Message, state : FSMContext):
    queues.remove_music_queue(9)