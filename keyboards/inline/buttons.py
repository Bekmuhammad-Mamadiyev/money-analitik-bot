from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


inline_keyboard = [[
    InlineKeyboardButton(text="✅ Yes", callback_data='yes'),
    InlineKeyboardButton(text="❌ No", callback_data='no')
]]
are_you_sure_markup = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

inline_keyboard = [[
    InlineKeyboardButton(text="✅ Ha", callback_data='yes'),
    InlineKeyboardButton(text="❌ Tahrirlash", callback_data='no')
]]
choise_data = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)