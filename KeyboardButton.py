from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
button_application = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Создать завку')
button_application.add(button_1)
