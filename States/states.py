
from aiogram.fsm.state import State, StatesGroup

class User_message(StatesGroup):
    message_photo = State()
    message_text = State()
    user_message = State()
