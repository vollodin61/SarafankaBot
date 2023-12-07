import logging

from environs import Env

from aiogram import Router, Dispatcher, Bot
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.fsm.storage.redis import RedisStorage


from redis.asyncio.client import Redis

from . import format_text_html as fth


url = 'http://redis://localhost:6379/0'
url2 = 'redis://localhost:6378/1'
logging.basicConfig(level=logging.INFO)
# logging.basicConfig(level=logging.ERROR)

env = Env()
env.read_env()
bot_token = env("TOKEN")
admins = list(map(lambda x: int(x), (env('ADMINS')).split(', ')))  # превращаем строку админов в список int

# red = Redis(host='rediska')  # Как это запустить, чтоб работало!! АААА!!!!!!!!
red = Redis(host='localhost')  # Как это запустить, чтоб работало!! АААА!!!!!!!!
red_storage = RedisStorage(red)  #
storage = MemoryStorage()
dp = Dispatcher(storage=red_storage)
bot = Bot(token=bot_token, parse_mode="HTML")
IP = env("ip")
PGUSER = env("PGUSER")
PGPASS = env("PGPASS")
PGDATA = env("PGDATA")
PGHOST = env("PGHOST")
PGPORT = env("PGPORT")
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASS}@{IP}/{PGDATA}"
postgres_url = f'postgresql+psycopg2://{PGUSER}:{PGPASS}@{PGHOST}:{PGPORT}/{PGDATA}'


class AvailableState(StatesGroup):
	st1 = State()
	st2 = State()
	st3 = State()
	st4 = State()

