import asyncio
import json

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.inline_all import profile_open_inl
from tgbot.data.loader import dp, bot
from tgbot.keyboards.reply_all import subcategory_menu, RETURN_BACK_TEXT, main_menu, product_menu


@dp.message_handler(text='Прайс лист')
async def send_price_list(message: Message):
    with open('tgbot/data/price.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    max_length = 4096
    parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]

    for i, part in enumerate(parts):
        if i % 5 == 0:
            await asyncio.sleep(3)
        await bot.send_message(chat_id=message.from_user.id, text=part)


global menu
with open('tgbot/data/price.json', 'r') as f:
    menu = json.load(f)


def update_menu():
    with open('tgbot/data/price.json', 'r') as f:
        content = json.load(f)
    menu.update(content)


@dp.message_handler(lambda message: message.text in menu.keys())
async def handle_category_click(message: Message):
    category = message.text
    keyboard = subcategory_menu(category)
    await message.answer(f"Выбери подкатегорию {category}:", reply_markup=keyboard)


@dp.message_handler(lambda message:
                    message.text in [subcategory for category in menu for subcategory in menu[category]]
                    or message.text == RETURN_BACK_TEXT)
async def handle_subcategory_click(message: Message):
    if message.text == RETURN_BACK_TEXT:
        await message.answer("Назад", reply_markup=main_menu(message.from_user.id))
    elif message.text == 'Samsung':
        cat = '📞Android'
        sub = 'Samsung'
        products = menu[cat][sub]
        text =''
        for product, data in products.items():
            prices = "\n".join(
                [f"{count} шт - {price}" for count, price in menu[cat][sub][product].items()])
            text += f"{product}\n\n{prices}\n\n"
        max_length = 4096
        parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
        for part in parts:
            await bot.send_message(chat_id=message.from_user.id, text=part)
    elif message.text == 'Все товары':
        cat = 'Другое'
        sub = 'Все товары'
        products = menu[cat][sub]
        text = ''
        for product, data in products.items():
            prices = "\n".join(
                [f"{count} шт - {price}" for count, price in menu[cat][sub][product].items()])
            text += f"{product}\n\n{prices}\n\n"
        max_length = 4096
        parts = [text[i:i + max_length] for i in range(0, len(text), max_length)]
        for part in parts:
            await bot.send_message(chat_id=message.from_user.id, text=part)
    else:
        for category in menu:
            if message.text in menu[category]:
                cat = category
                subcategory = message.text
                break
        keyboard = product_menu(cat, subcategory)
        await message.answer(f"Вы выбрали {subcategory}.", reply_markup=keyboard)


@dp.message_handler(
    lambda message: message.text in [product for category in menu for subcategory in menu[category] for product in
                                     menu[category][subcategory]])
async def product_handler(message: Message):
    for category in menu:
        for subcategory in menu[category]:
            if message.text in menu[category][subcategory]:
                cat = category
                sub = subcategory
                product = message.text
                break
    prices = "\n".join(
        [f"{count} шт - {price}" for count, price in menu[cat][sub][product].items()])
    text = f"{product}\n\n{prices}"
    await message.answer(text)
