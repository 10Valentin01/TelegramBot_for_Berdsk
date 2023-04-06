# importing the necessary libraries
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import CommandStart

from config import TOKEN, intodaction

bot = Bot(token=TOKEN)

dp = Dispatcher(bot)

@dp.message_handler(CommandStart())
async def start_func(message: types.Message):
    await message.answer(intodaction)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)