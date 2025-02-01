import pandas as pd
from aiogram import Router, F
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from utils.pgtoexcel import export_revenue_to_excel
from aiogram import types
from loader import db
import os
router = Router()


@router.message(F.text == "📈 Daromadlarni ko‘rish")
async def show_revenue(message: Message, state: FSMContext):

    revenues = await db.get_user_revenues(message.from_user.id)

    if not revenues:
        await message.answer("Sizda hech qanday daromadlar mavjud emas.")
        return

    # Daromadlarni eksport qilish uchun faylni yaratish
    file_path = f"data/revenues_{message.from_user.id}.xlsx"
    await export_revenue_to_excel(
        data=[(revenue['amount'], revenue['reason'], revenue['date']) for revenue in revenues],
        headings=['Amount', 'Reason', 'Date'],
        filepath=file_path
    )

    # Foydalanuvchiga Excel faylini yuborish
    await message.answer_document(types.input_file.FSInputFile(file_path))

    # Ixtiyoriy: Faylni serverdan o‘chirish
    os.remove(file_path)

    await state.clear()



