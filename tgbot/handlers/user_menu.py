import json

from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from tgbot.keyboards.inline_all import profile_open_inl
from tgbot.data.loader import dp
from tgbot.keyboards.reply_all import subcategory_menu, RETURN_BACK_TEXT, main_menu, product_menu

with open('tgbot/data/price.json', 'r') as f:
    menu = json.load(f)


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
        [f"🇷🇺 От {count} шт - {price}" for count, price in menu[cat][sub][product].items()])
    text = f"{product}\n\n{prices}"
    await message.answer(text)
