from aiogram import types, Router
from aiogram.filters import Command, Text
from keyboards import user_kb as kb
from database.admin_db import cmd_start_db

router = Router()


@router.message(Command('start'))
async def cmd_start(message: types.Message):
    await cmd_start_db(message.from_user.id)
    await message.answer(f'Здравствуйте, <b>{message.from_user.first_name}</b>', reply_markup=kb.main)
    
    
@router.message(Text('Блюда по национальности'))
async def cmd_start(message: types.Message):
    await message.answer(f'Выберите вариант', reply_markup=kb.nat.as_markup())
    
    
@router.message(Text('Блюда по магазину'))
async def cmd_start(message: types.Message):
    await message.answer(f'Выберите вариант', reply_markup=kb.shop.as_markup())
    
    
@router.message(Text('Блюда по скорости'))
async def cmd_start(message: types.Message):
    await message.answer(f'Выберите вариант', reply_markup=kb.speed.as_markup())
    

@router.callback_query(Text('italy'))
async def cmd_start(callback: types.CallbackQuery):
    await callback.message.answer(f'Выберите категорию', reply_markup=kb.italy.as_markup())
    
    
@router.callback_query(Text('pizza'))
async def cmd_start(callback: types.CallbackQuery):
    await callback.message.answer(f'<b>Ветчина-грибы</b>\n\n'
                                  f'Ингридиенты для теста: Вода питьевая!\n'
                                  f'250 граммов, Соль 12 граммов, Оливковое масло 15 граммов, Мука высшего сорта 400 граммов,Живые 15 гр или сухие 6гр дрожжи.\n'
                                  f'Готовим основу для пиццы.\n'
                                  f'В воде вручную хорошенько размешиваем соль, добавляем оливковое масло, дрожжи и муку.\n', reply_markup=kb.back)
    
    
@router.message(Text('Назад'))
async def cmd_start(message: types.Message):
    await message.answer(f'Вы вернулись в основное меню', reply_markup=kb.main)
