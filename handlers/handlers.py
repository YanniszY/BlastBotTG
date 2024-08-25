from aiogram import Bot, Dispatcher, Router, F, types
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
import asyncio

from chat_list import channel_ids
from Keyboard.kb import kb, skip_btn
from States.states import User_message
from util.func import send_user_message


admin_id = 0 # telegram admin id

router = Router()

@router.message(CommandStart())
async def start(message: Message):
    if message.from_user.id == admin_id: #
        await message.answer("Привет! Добавь свое сообщение и начни рассылку по чатам!\n\n!ВАЖНО! рассылка будет происходить только в тех чатах в которых добавлен этот бот.", reply_markup=kb)
    else:
        message.answer("У вас нет доступа к этому боту!")


@router.callback_query(F.data == 'add_message')
async def add_message(callback_query: CallbackQuery, state: FSMContext):
    await state.clear()
    await state.set_state(User_message.message_photo)
    await callback_query.message.answer("отправь фотографию или видео (необезательно)", reply_markup=skip_btn)


@router.message(User_message.message_photo)
async def get_or_skip_photo(message: Message, state: FSMContext):
    if message.text == "Пропустить":
        await state.clear()
        await message.answer("Теперь напиши текст")
        await state.set_state(User_message.message_text)
    elif message.photo: #  or message.video
        await message.answer("Получено! Теперь напиши текст")
        await state.update_data(message_photo=message.photo[-1].file_id)
        await state.set_state(User_message.message_text)


# Хэндлер для получения текста сообщения
@router.message(User_message.message_text)
async def get_message_text(message: Message, state: FSMContext):
    await state.update_data(message_text=message.text)
    data = await state.get_data()
    await message.answer("Готово")
    await send_user_message(message, data)



@router.callback_query(F.data == 'show_message')
async def show_message(callback_query: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_text = data.get('message_text')
    user_media = data.get('message_photo')

    await callback_query.message.answer("Ваше сообщение:")

    # Проверяем, что user_text не None
    if user_media:
        # Если есть медиа и текст, отправляем оба
        await callback_query.message.answer_photo(photo=user_media, caption=user_text or "")
    elif user_text:
        # Если только текст, отправляем текст
        await callback_query.message.answer(user_text)
    else:
        # Если нет ни текста, ни медиа, отправляем сообщение об ошибке
        await callback_query.message.answer("Сообщение не найдено. Пожалуйста, отправьте сообщение.")


@router.callback_query(F.data == 'start_spam')
async def start_spam(callback_query: CallbackQuery, state: FSMContext, bot: Bot):
    data = await state.get_data()
    user_text = data.get('message_text')
    user_media = data.get('message_photo')

    for channel_id in channel_ids:

        if user_media:
            await bot.send_photo(chat_id=channel_id, photo=user_media, caption=user_text)
        else:
            await bot.send_message(chat_id=channel_id, text=user_text)
                
        await callback_query.message.answer(f"Сообщение успешно отправлено в {channel_id}")



    await callback_query.message.answer("Рассылка завершена.")


def register_handlers(router: Dispatcher, bot: Bot):
    async def start_spam_callback(callback_query: CallbackQuery, state: FSMContext):
        await start_spam(callback_query, state, bot)
    
    router.callback_query.register(start_spam_callback, F.data == 'start_spam')


@router.message()
async def error(message: Message):
    await message.answer("Ошибка. Попробуйте еще раз!")
