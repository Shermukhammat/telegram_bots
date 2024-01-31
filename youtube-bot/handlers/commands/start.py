from loader import dp, db, types, media_text
from aiogram.dispatcher import FSMContext



@dp.message_handler(commands = 'start', state = "*")
async def start_message_handler(update : types.Message):
    if db.is_user(id = update.from_user.id):
        # await update.answer("You are user")
        user = db.users[update.from_user.id]
        print(user)
        # print(media_text.welcome_user(user))
    
    elif db.is_admin(id  = update.from_user.id):
        await update.answer("You are admin")
        

    else:
        db.registir(id = update.from_user.id, 
                    name = update.from_user.first_name, 
                    lang = update.from_user.language_code)
        
        # text = context.welcome_user(db.users[update.from_user.id])
        # print(text)
        # print(db.users[update.from_user.id])
        # await update.answer(context.welcome_user(db.users[update.from_user.id]))
    
