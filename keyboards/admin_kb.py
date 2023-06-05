from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from database.admin_db import get_all_items

main_kb = [
    [KeyboardButton(text='Блюда по национальности')],
    [KeyboardButton(text='Блюда по магазину')],
    [KeyboardButton(text='Блюда по скорости')],
    [KeyboardButton(text='Контакты')],
    [KeyboardButton(text='Админ-панель')]
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')


adminka_kb = [
    [KeyboardButton(text='Создать товар')],
    [KeyboardButton(text='Изменить товар')],
    [KeyboardButton(text='Удалить товар')],    
]


adminka = ReplyKeyboardMarkup(keyboard=adminka_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

def get_all_items_kb():
    items = get_all_items()
    items_list = []
    for i in items:
        items_list.append([InlineKeyboardButton(text=i[1], callback_data=i[0])])
    items_all_kb = InlineKeyboardMarkup(inline_keyboard=items_list)
    return items_all_kb


def type_of_edit_kb():
    items_list = []
    items_list.append([InlineKeyboardButton(text='Название', callback_data='name')])
    items_list.append([InlineKeyboardButton(text='Описание', callback_data='desc')])
    items_list.append([InlineKeyboardButton(text='Фото', callback_data='photo')])
    items_list.append([InlineKeyboardButton(text='Цену', callback_data='price')])
    items_all_kb = InlineKeyboardMarkup(inline_keyboard=items_list)
    return items_all_kb
# ======================================================================================================

admin_kb = [
    [KeyboardButton(text='Работа с товаром')],
    [KeyboardButton(text='Сделать рассылку')],
]


admin = ReplyKeyboardMarkup(keyboard=admin_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

# ======================================================================================================
