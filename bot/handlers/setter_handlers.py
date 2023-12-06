from aiogram import Dispatcher

# from bot.config.cfg import dp
from .default import def_router
from .custom import cust_router


def set_routers(dp: Dispatcher):
	dp.include_router(def_router)
	dp.include_router(cust_router)
