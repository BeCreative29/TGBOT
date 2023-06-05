from aiogram import types, Router, F
from typing import Callable, Dict, Any, Awaitable
from aiogram.filters import Command, Text
from keyboards import admin_kb as kb
from database.admin_db import *
from aiogram import Bot
from run import bot
from aiogram.types import ReplyKeyboardRemove
from aiogram.filters.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram import BaseMiddleware

router = Router()


class AdminCheck(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[types.Message, Dict[str, Any]], Awaitable[Any]],
        event: types.Message,
        data: Dict[str, Any]):

        if event.from_user.id in [935898133, 123]:
            return await handler(event, data)


router.message.outer_middleware(AdminCheck())


class Rassilka(StatesGroup):
    send = State()

    
class Create(StatesGroup):
    name = State()
    desc = State()
    photo = State()
    price = State()
    

class Change(StatesGroup):
    items_list_state = State()
    type_of_edit = State()
    name = State()
    desc = State()
    photo = State()
    price = State()
    
    
class Delete(StatesGroup):
    items_list_state = State()
    type_of_edit = State()
    name = State()
    desc = State()
    photo = State()
    price = State()

"""
БАЗОВЫЕ КОМАНДЫ
"""

@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await cmd_start_db(message.from_user.id)
    await message.answer(f'Здравствуйте, <b>{message.from_user.first_name}</b>', reply_markup=kb.main)

"""
АДМИН-ПАНЕЛЬ
"""

@router.message(Text('Админ-панель'))
async def cmd_start(message: types.Message):
    await message.answer(f'Выберите вариант', reply_markup=kb.admin)


@router.message(Text('Работа с товаром'))
async def cmd_start(message: types.Message):
    await message.answer(f'Выберите вариант', reply_markup=kb.adminka)

"""
СОЗДАНИЕ ТОВАРА
"""
#=======================================================================

@router.message(Text('Создать товар'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Create.name)
    await message.answer(f'Напишите название товара', reply_markup=ReplyKeyboardRemove())


@router.message(Create.name)
async def cmd_start(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Create.desc)
    await message.answer(f'Введите описание товара')


@router.message(Create.desc)
async def cmd_create(message: types.Message, state: FSMContext):
    await state.update_data(desc=message.text)
    await state.set_state(Create.photo)
    await message.answer(f'Отправьте фото товара')


@router.message(lambda m: not m.photo, Create.photo)
async def cmd_create(message: types.Message, state: FSMContext):
    await message.answer(f'Это не фотография! Отправьте фото')


@router.message(Create.photo, F.photo)
async def cmd_create(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    await state.set_state(Create.price)
    await message.answer(f'Введите стоимость товара')


@router.message(Create.price)
async def cmd_create(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    info = await state.get_data()
    await add_item_db(info)
    await state.clear()
    await message.answer(f'Товар успешно создан!', reply_markup=kb.admin)


#=======================================================================
"""
Изменение товара
"""

@router.message(Text('Изменить товар'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Change.items_list_state)
    await message.answer(f'Выберите товар', reply_markup=kb.get_all_items_kb())


@router.callback_query(Change.items_list_state)
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.update_data(one_of=callback.data)
    about_item = await get_one_item(callback.data)
    await state.set_state(Change.type_of_edit)
    await callback.message.answer(f'Вы выбрали товар: {about_item[1]}\n\n'
                                  f'Что вы хотели бы изменить?', reply_markup=kb.type_of_edit_kb())

# Изменение названия
# ===========================================

@router.callback_query(Change.type_of_edit, lambda c: c.data == 'name')
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Change.name)
    await callback.message.answer(f'Введите новое название товара')


@router.message(Change.name)
async def cmd_create(message: types.Message, state: FSMContext):
    item_i = await state.get_data()
    await edit_name(item_i['one_of'], message.text)
    await state.clear()
    await message.answer(f'Название товара изменено!', reply_markup=kb.admin)

# Изменение описания
# ===========================================

@router.callback_query(Change.type_of_edit, lambda c: c.data == 'desc')
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Change.desc)
    await callback.message.answer(f'Введите новое описание товара')


@router.message(Change.desc)
async def cmd_create(message: types.Message, state: FSMContext):
    item_i = await state.get_data()
    await edit_desc(item_i['one_of'], message.text)
    await state.clear()
    await message.answer(f'Описание товара изменено!', reply_markup=kb.admin)

# ===========================================

@router.message(lambda m: not m.photo, Change.photo)
async def cmd_create(message: types.Message, state: FSMContext):
    await message.answer(f'Это не фотография! Отправьте фото')


@router.callback_query(Change.type_of_edit, lambda c: c.data == 'photo')
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Change.photo)
    await callback.message.answer(f'Вставьте новое фото товара')


@router.message(Change.photo)
async def cmd_create(message: types.Message, state: FSMContext):
    item_i = await state.get_data()
    await edit_photo(item_i['one_of'], message.photo[-1].file_id)
    await state.clear()
    await message.answer(f'Фото изменено!', reply_markup=kb.admin)
    
# ===========================================

@router.callback_query(Change.type_of_edit, lambda c: c.data == 'price')
async def cmd_start(callback: types.CallbackQuery, state: FSMContext):
    await state.set_state(Change.price)
    await callback.message.answer(f'Введите новую стоимость товара')


@router.message(Change.price)
async def cmd_create(message: types.Message, state: FSMContext):
    item_i = await state.get_data()
    await edit_price(item_i['one_of'], message.text)
    await state.clear()
    await message.answer(f'Стоимость изменена!', reply_markup=kb.admin)

#=======================================================================
 
@router.message(Text('Удалить товар'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Delete.type_of_edit)
    await message.answer(f'Выберите вариант', reply_markup=kb.get_all_items_kb())


@router.callback_query(Delete.type_of_edit)
async def cmd_create(callback: types.CallbackQuery, state: FSMContext):
    await delete_item(callback.data)
    await state.clear()
    await callback.answer(f'Товар успешно удален!', reply_markup=kb.admin)

#=======================================================================

@router.message(Text('Сделать рассылку'))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.set_state(Rassilka.send)
    await message.answer(f'Введите сообщение для рассылки', reply_markup=ReplyKeyboardRemove())


@router.message(Rassilka.send)
async def cmd_rassilka(message: types.Message, state: FSMContext):
    users = await select_all()
    for i in users:
        await bot.send_message(i[0], text=message.text)
    await state.clear()
    await message.answer('Рассылка завершена!', reply_markup=kb.admin)
