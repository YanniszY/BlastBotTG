import asyncio

from aiogram.types import Message




async def send_user_message(message: Message, data: dict):
    user_text = data.get('message_text')
    user_media = data.get('message_photo')
    
    if user_media: # Если есть медиа, отправляем его вместе с текстом
        await message.answer_photo(photo=user_media, caption=user_text)
    else:  # Если медиа нет, отправляем только текст
        await message.answer(user_text)
