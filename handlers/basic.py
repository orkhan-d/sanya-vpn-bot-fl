from aiogram import Router, types, F
from aiogram.filters import CommandStart

from db.crud.texts import get_text
from db.crud.users import create_user
from keyboards.basic import start_keyboard

router = Router()


@router.message(CommandStart())
async def on_start(message: types.Message):
    invited_by: int | None = None
    if invited_by_id := message.text.replace('/start', '').strip():
        invited_by = int(invited_by_id)
    create_user(
        message.from_user.id,
        message.from_user.full_name,
        message.from_user.username,
        invited_by
    )
    await message.answer(get_text('start'),
                         reply_markup=start_keyboard)


@router.callback_query(F.data == 'start')
async def on_start(query: types.CallbackQuery):
    await query.message.answer(get_text('start'),
                               reply_markup=start_keyboard)
