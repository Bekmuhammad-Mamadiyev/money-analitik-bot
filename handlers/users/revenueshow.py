from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from loader import db
from aiogram import types

from utils.pgtoexcel import export_to_excel

router = Router()

@router.message(F.text == "📈 Daromadlarni ko‘rish")
async def show_revenue(message: Message, state: FSMContext):
    revenues = await db.get_user_revenues(message.from_user.id)
    if not revenues:
        await message.answer("Sizning daromadlaringiz yo'q!")
        return

    filepath = f"data/revenue_{message.from_user.id}.xlsx"

    await export_to_excel(data=[(revenue['amount'], revenue['reason'],revenue['date']) for revenue in revenues],
                          headings=['Miqdor', 'Sabab', 'Sanasi'], filepath=filepath)
    await message.answer_document(types.input_file.FSInputFile(filepath))

    await state.clear()


