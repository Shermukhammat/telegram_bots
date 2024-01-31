from aiogram.dispatcher.filters.state import StatesGroup, State





class Registr(StatesGroup):
    chose_lang = State()





class States:
    def __init__(self) -> None:
        chos = None