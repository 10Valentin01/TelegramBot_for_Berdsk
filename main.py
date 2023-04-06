# importing the necessary libraries
import time
import sqlite3
import logging

from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart, Text
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.dispatcher import FSMContext
from aiogram.types import ReplyKeyboardRemove

from config import TOKEN, intodaction
from KeyboardButton import *
from State_test import Applications
from DataClass import Database

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=storage)

count_app = 0

db = Database()
try:
    db.create_table_users()
    print('Таблица создана')
except Exception as e:
    print(e)

@dp.message_handler(CommandStart(), state=None)
async def start_func(message: types.Message):
    await message.answer(intodaction, reply_markup=button_application)
    await Applications.num_app.set()

@dp.message_handler(Text(equals='Новая заявка'), state=None)
async def start_func(message: types.Message):
    await message.answer('Нажмите "Создать заявку"', reply_markup=button_application)
    await Applications.num_app.set()

@dp.message_handler(Text(equals='Создать заявку'), state=Applications.num_app)
async def applications(message: types.Message, state: FSMContext):

    global count_app
    count_app += 1
    async with state.proxy() as data:
        data['num_app'] = f'Заявка номер: {count_app}'
    await message.answer(f'Создана заявка номер: {count_app}')
    await message.answer(f'Выберите тему', reply_markup=button_topic)
    await Applications.next()


@dp.message_handler(Text(equals=['Конализация', 'Дороги', 'Электричество']), state=Applications.topic)
async def topic_choose(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['topic'] = message.text
    await message.answer(f'Пожалуйста, опишите проблему более подробно')
    await Applications.next()

@dp.message_handler(state=Applications.applications)
async def applications_about(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['applications'] = message.text
    await message.answer('Благодарю Вас за то, что описали все подробробно')
    time.sleep(1)
    await message.answer('Укажите Ваше ФИО')
    await Applications.next()

@dp.message_handler(state=Applications.name)
async def applications_about(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
    await message.answer('Приятно познакомиться')
    time.sleep(1)
    await message.answer('Укажите Ваш адрес')
    await Applications.next()

@dp.message_handler(state=Applications.address)
async def applications_about(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['address'] = message.text
    await message.answer('Благодарю, остался один шаг до завершения')
    time.sleep(1)
    await message.answer('Укажите Ваш телефон')
    await Applications.next()

@dp.message_handler(state=Applications.phone)
async def applications_about(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
        db.add_app(id=int(data['num_app'][-1]), num_app=data['num_app'], topic=data['topic'], name=data['name'],
                   address=data['address'], phone=data['phone'], application=data['applications'])
    await message.answer('Поздравляю! Ваша заявка создана, ожидайте звонка оператора', reply_markup=button_new_app)

    await state.reset_state()





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)