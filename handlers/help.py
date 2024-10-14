from aiogram import Router, F, types

from db.crud.texts import get_text
from keyboards import help as kb

router = Router()


@router.callback_query(F.data == 'help')
async def on_start(query: types.CallbackQuery):
    # TODO: set support account in text
    await query.message.answer(get_text('help'),
                               reply_markup=kb.help_kb)


@router.callback_query(F.data == 'rules')
async def on_start(query: types.CallbackQuery):
    await query.message.answer(get_text('rules'),
                               reply_markup=kb.rules_kb)
