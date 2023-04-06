# importing the necessary libraries
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart


from config import TOKEN, intodaction
from KeyboardButton import *
bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start_func(message: types.Message):
    await message.answer(intodaction, reply_markup=button_application)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)