from redis import Redis
from redis.cluster import RedisCluster
from config.cfg import red_storage
import asyncpg
import psycopg2
from sqlalchemy import create_engine
from environs import Env


env = Env()
env.read_env()
bot_token = env("TOKEN")
admins = list(map(lambda x: int(x), (env('ADMINS')).split(', ')))  # превращаем строку админов в список int
IP = env("ip")
PGUSER = env("PGUSER")
PGPASS = env("PGPASS")
PGDATA = env("PGDATA")
PGHOST = env("PGHOST")
PGPORT = env("PGPORT")
POSTGRES_URI = f"postgresql://{PGUSER}:{PGPASS}@{PGHOST}/{PGDATA}"

engine = create_engine(f'postgresql+psycopg2://{PGUSER}:{PGPASS}@{PGHOST}:{PGPORT}/{PGDATA}', echo=True)
engine.connect()

print(engine)



# r = Redis(decode_responses=True)
# r.hset(name='goodbye', mapping={
# 	'1': 'goodbye',
# 	'2': 'goodluck',
# 	'3': 'goodfuck'
# })
#
# print(r.hgetall(name='goodbye'))

from time import sleep

sleep