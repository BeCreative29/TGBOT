from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

main_kb = [
    [KeyboardButton(text='Блюда по национальности')],
    [KeyboardButton(text='Блюда по магазину')],
    [KeyboardButton(text='Блюда по скорости')],
    [KeyboardButton(text='Контакты')],
]

main = ReplyKeyboardMarkup(keyboard=main_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пункт меню...')

nat = InlineKeyboardBuilder()
nat.row(InlineKeyboardButton(text='Италия', callback_data='italy'),
        InlineKeyboardButton(text='Франция', callback_data='france'))
nat.row(InlineKeyboardButton(text='Япония', callback_data='japan'),
        InlineKeyboardButton(text='Грузия', callback_data='georgian'),
        InlineKeyboardButton(text='Паназития', callback_data='panasia'))

shop = InlineKeyboardBuilder()
shop.row(InlineKeyboardButton(text='Магнит', callback_data='magnit'),
        InlineKeyboardButton(text='Метро', callback_data='metro'))
shop.row(InlineKeyboardButton(text='Пятерочка', callback_data='pyaterochka'),
        InlineKeyboardButton(text='Ашан', callback_data='ashan'),
        InlineKeyboardButton(text='Лента', callback_data='lenta'),
        InlineKeyboardButton(text='Перекресток', callback_data='perekrestok'))
        
speed = InlineKeyboardBuilder()
speed.row(InlineKeyboardButton(text='10 минут', callback_data='10min'),
        InlineKeyboardButton(text='15 минут', callback_data='15min'))
speed.row(InlineKeyboardButton(text='20 минут', callback_data='20min'),
        InlineKeyboardButton(text='30 минут', callback_data='30min'),
        InlineKeyboardButton(text='60 минут', callback_data='60min'),
        InlineKeyboardButton(text='12 часов', callback_data='12hours'))

italy = InlineKeyboardBuilder()
italy.row(InlineKeyboardButton(text='Пицца', callback_data='pizza'),
        InlineKeyboardButton(text='Ризотто', callback_data='rizotto'))
italy.row(InlineKeyboardButton(text='Паста', callback_data='paste'),
        InlineKeyboardButton(text='Ньокки', callback_data='gnocchi'),
        InlineKeyboardButton(text='Салаты', callback_data='salads'),
        InlineKeyboardButton(text='Супы', callback_data='soups'))

back_kb = [
    [KeyboardButton(text='Назад')]
]

back = ReplyKeyboardMarkup(keyboard=back_kb,
                           resize_keyboard=True,
                           input_field_placeholder='Назад')
