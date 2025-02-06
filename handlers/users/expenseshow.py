from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from loader import db
from aiogram import types

from utils.pgtoexcel import export_to_excel

router = Router()

@router.message(F.text == "📊 Xarajatlarni ko‘rish")
async def show_expense(message: Message, state: FSMContext):
    expenses = await db.get_user_expense(message.from_user.id)
    if not expenses:
        await message.answer("Sizning Xarajatlaringiz yo'q!")
        return

    filepath = f"data/expense_{message.from_user.id}.xlsx"

    await export_to_excel(data=[(expense['amount'], expense['expense'],expense['date']) for expense in expenses],
                          headings=['Miqdor', 'Sabab', 'Sanasi'], filepath=filepath)
    await message.answer_document(types.input_file.FSInputFile(filepath))

    await state.clear()


