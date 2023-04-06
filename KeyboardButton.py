from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
# Кнопка с созданием заявки
button_application = ReplyKeyboardMarkup(resize_keyboard=True)
button_1 = KeyboardButton(text='Создать заявку')
button_application.add(button_1)

# Кнопки с темами заявок
button_topic = ReplyKeyboardMarkup(resize_keyboard=True)
button_2 = KeyboardButton(text='Конализация')
button_3 = KeyboardButton(text='Дороги')
button_4 = KeyboardButton(text='Электричество')
button_topic.add(button_2, button_3, button_4)