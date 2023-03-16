from aiogram.types import Message, ContentTypes

from tgbot.data.config import get_admins
from tgbot.data.loader import dp, bot
from tgbot.handlers.user_menu import update_menu
from tgbot.services.data_to_json import main
from tgbot.utils.misc.bot_filters import IsAdmin


@dp.message_handler(text='Добавить прайс')
async def ask_to_send_file(message: Message):
    if message.from_user.id in get_admins():
        await message.answer("Пришли файл прайс листа")


@dp.message_handler(content_types=ContentTypes.DOCUMENT)
async def get_file_from_user(message: Message):
    if message.from_user.id in get_admins():
        file_id = message.document.file_id
        file = await bot.get_file(file_id)

        file_path = f"tgbot/data/price.txt"
        await file.download(file_path)
        main()
        update_menu()

        await message.answer("Файл успешно загружен.")
