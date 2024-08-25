
from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    ReplyKeyboardMarkup,
    KeyboardButton
)

kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Написать сообщение для рассылки", callback_data="add_message")], # 4
        [InlineKeyboardButton(text="Показать мое сообщение", callback_data="show_message")], # 2
        [InlineKeyboardButton(text="Начать рассылку", callback_data="start_spam")], # 1
    ]
)

skip_btn = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Пропустить")]
    ]
)