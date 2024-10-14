from aiogram import Router, types, F

from db.crud.texts import get_text
import keyboards.tutors as kb
from db.crud.users import get_user_by_id

router = Router()


@router.callback_query(F.data.endswith('_tutor'))
async def on_start(query: types.CallbackQuery):
    user = get_user_by_id(query.from_user.id)
    await query.message.answer(get_text(query.data).format(link=user.subscription_link),
                               reply_markup=kb.after_tutor_kb)
