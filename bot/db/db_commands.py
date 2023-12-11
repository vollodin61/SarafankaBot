from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy import select

from bot.garb import Parent, Child
from db_models import engine, User, Courses, Webinars


session = sessionmaker(bind=engine)

with session(autoflush=False, bind=engine) as ses:
	a = User()
	ses.add(a)
	ses.commit()