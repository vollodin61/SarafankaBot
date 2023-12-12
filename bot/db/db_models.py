from typing import List

import sqlalchemy
from sqlalchemy import (create_engine, MetaData, Table, Integer,
						String, Column, DateTime, ForeignKey, ForeignKeyConstraint, Numeric, Text, Boolean)
from sqlalchemy.orm import declarative_base, relationship, mapped_column, Mapped
from datetime import datetime

from bot.config.cfg import postgres_url

# engine = create_engine(postgres_url)  # это движок для работы с бд
									#  12345678 - это пароль для пользователя i
engine = create_engine("postgresql+psycopg2://i:12345678@localhost:5432/sarafan_db", echo=True)  # Если тут добавить Echo=True то будет выводить лог
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
	user_id = mapped_column(Integer, primary_key=True)
	telegram_id = Column(Integer, unique=True)
	username = Column(String(255))
	status = Column(String(255))
	first_name = Column(String(255))
	last_name = Column(String(255))
	description = Column(String())
	u_course: Mapped[int] = mapped_column(ForeignKey('courses.course_id'))
	# u_webinars = Column(Integer, ForeignKey('webinars.webinar_id'))
	user_courses: Mapped['Courses'] = relationship(back_populates='user')
	# user_webinars = relationship("Webinars", back_populates='user')

	# __table_args__ = (
	# 	ForeignKeyConstraint(['user_id'], ['course_id']),
	# )


class Courses(BaseClass):
	__tablename__ = 'courses'
	course_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
	name = Column(String(255), unique=True)
	user: Mapped[List['User']] = relationship(back_populates='user_courses')


class Webinars(BaseClass):
	__tablename__ = 'webinars'
	webinar_id = Column(Integer, primary_key=True, autoincrement=True, unique=True, index=True)
	name = Column(String(255), unique=True)
	# user = relationship('User', )


# class Otz(BaseClass):
# 	pass
#
#
# class Polls(BaseClass):
# 	pass
#
#
# class Club(BaseClass):
# 	pass
Base.metadata.create_all(engine)

# try:
# 	Base.metadata.create_all(engine)
# except Exception:
# 	from psycopg2 import connect
# 	from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
#
# 	connection = connect(user='i', password='12345678')
# 	connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
# 	cursor = connection.cursor()
# 	sql_database = cursor.execute('create database sqlalchemy_tuts')
# 	cursor.close()
# 	connection.close()
