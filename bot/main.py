import asyncio
import logging

from aiogram import Bot, Dispatcher, html, F
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandObject, CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.base import BaseStorage
from aiogram.types import Message, FSInputFile, URLInputFile, BufferedInputFile, CallbackQuery, ReplyKeyboardRemove
from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardButton, ReplyKeyboardBuilder, KeyboardBuilder
from aiogram.utils.formatting import as_list, as_marked_section, Bold, as_key_value, HashTag
from aiogram.utils.markdown import hide_link
from aiogram.utils.media_group import MediaGroupBuilder

from config.cfg import bot, dp
from commands.setter import set_commands
from handlers import set_routers


async def main():
	logging.basicConfig(level=logging.INFO)
	set_routers(dp)
	await set_commands(bot)
	await bot.delete_webhook(drop_pending_updates=True)
	await dp.start_polling(bot)


if __name__ == "__main__":
	asyncio.run(main())
