from aiogram.dispatcher.filters.state import StatesGroup, State

class Applications(StatesGroup):
    num_app = State()
    topic = State()
    applications = State()
    name = State()
    address = State()
    phone = State()