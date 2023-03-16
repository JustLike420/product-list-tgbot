import json

from aiogram.types import ReplyKeyboardMarkup

from tgbot.data.config import get_admins

RETURN_BACK_TEXT = "⬅ Назад"


def main_menu(user_id):
    keyboard = ReplyKeyboardMarkup()
    keyboard.row("Прайс лист")
    with open('tgbot/data/price.json', 'r') as f:
        menu = json.load(f)
        for category in menu.keys():
            keyboard.row(category)

    if user_id in get_admins():
        keyboard.row("Добавить прайс-лист")
    return keyboard


def subcategory_menu(category):
    keyboard = ReplyKeyboardMarkup()
    with open('tgbot/data/price.json', 'r') as f:
        menu = json.load(f)
    for subcategory in menu[category]:
        keyboard.row(subcategory)
    keyboard.row(RETURN_BACK_TEXT)
    return keyboard


def product_menu(category, subcategory):
    keyboard = ReplyKeyboardMarkup()
    with open('tgbot/data/price.json', 'r') as f:
        menu = json.load(f)
    for product in menu[category][subcategory]:
        keyboard.row(product)
    keyboard.row(RETURN_BACK_TEXT)
    return keyboard


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")
