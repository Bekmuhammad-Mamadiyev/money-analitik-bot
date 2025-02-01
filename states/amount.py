from aiogram.filters.state import StatesGroup, State


class ExpenseState(StatesGroup):
    amount = State()
    reason = State()
    date_confirmation = State()
    new_date = State()


class RevenueState(StatesGroup):
    amount = State()
    reason = State()
    date_confirmation = State()
    new_date = State()