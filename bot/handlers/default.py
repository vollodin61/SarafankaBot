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
		await message.answer(text='СТАРТУЕМ!', parse_mode=ParseMode.HTML)
		await state.set_state(Avs.st1)
		await state.set_data({'text': message.text, 'user_id': f'{message.from_user.id}'})
		print(await state.get_data())

	except Exception as exc:
		print(exc)
