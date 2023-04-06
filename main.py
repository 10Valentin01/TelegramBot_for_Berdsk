# importing the necessary libraries
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart, Text


from config import TOKEN, intodaction
from KeyboardButton import *
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

count_app = 0

dict_application = {}
@dp.message_handler(CommandStart())
async def start_func(message: types.Message):
    await message.answer(intodaction, reply_markup=button_application)


@dp.message_handler(Text(equals='Создать заявку'))
async def applications(message: types.Message):
    global count_app
    count_app += 1
    id = message.from_user.id
    dict_application[id] = []
    dict_application[id].append(f'Создана заявка номер: {count_app}')
    await message.answer(f'Создана заявка номер: {count_app}')
    print(dict_application)
    await message.answer(f'Выберите тему', reply_markup=button_topic)

@dp.message_handler(Text(equals=['Конализация', 'Дороги', 'Электричество']))
async def topic_choose(message: types.Message):
    id = message.from_user.id
    dict_application[id].append(message.text)
    print(dict_application)
    await message.answer(f'Опишите подробнее проблему')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)