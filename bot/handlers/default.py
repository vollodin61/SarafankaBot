import logging

from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.enums import ParseMode

from bot.config.cfg import AvailableState as Avs
from bot.data.smiles import Texts as Txt


def_router = Router()


@def_router.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
	try:
		# logging.basicConfig(level=logging.INFO)  ЭТО В КОНФИГЕ ПРОПИСАНО
		await message.answer(text='СТАРТУЕМ!', parse_mode=ParseMode.HTML)
		await state.set_state(Avs.st1)
		await state.set_data({'text': message.text, 'user_id': f'{message.from_user.id}'})
		data = await state.get_data()
		await message.answer(str(data))
		await message.answer(text='safasdf')

	except Exception as exc:
		print(exc)
