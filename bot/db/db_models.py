from sqlalchemy import create_engine, MetaData, Table, Integer, String, Column, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import declarative_base
from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from datetime import datetime

from bot.config.cfg import postgres_url

# engine = create_engine(postgres_url)  # это движок для работы с бд
engine = create_engine("postgresql+psycopg2://postgres:12345678@localhost:5432/sqlalchemy_tuts", echo=True)
# engine = create_engine(postgres_url, echo=True)

# engine.connect()
# print(engine)
#
# connection = connect(user='postgres', password='12345678')
# connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

# cursor = connection.cursor()
# # create_database = cursor.execute('create database sqlalchemy_tuts')
# cursor.close()
# connection.close()

Base = declarative_base()


class BaseClass(Base):
	__abstract__ = True  # ХЗ может быть тут это не нужно

	created_at = Column(DateTime(), default=datetime.now())
	updated_at = Column(DateTime(), default=datetime.now(), onupdate=datetime.now())


class User(BaseClass):
	__tablename__ = 'users'
	user_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
	telegram_id = Column(Integer, primary_key=True, unique=True)
	username = Column(String(255))
	status = Column(String(255))
	first_name = Column(String(255))
	last_name = Column(String(255))
	description = Column(String())


class Courses(BaseClass):
	__tablename__ = 'courses'
	course_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
	name = Column(String(255), unique=True)


class Webinars(BaseClass):
	__tablename__ = 'webinars'
	webinar_id = Column(Integer, primary_key=True, autoincrement=True, unique=True)
	name = Column(String(255), unique=True)


Base.metadata.create_all(engine)