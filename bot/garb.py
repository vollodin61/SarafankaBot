from __future__ import annotations
from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import DeclarativeBase, declarative_base
from sqlalchemy.orm import relationship

from bot.db.db_models import engine

Base = declarative_base()


class Parent(Base):
	__tablename__ = "parent_table"

	id: Mapped[int] = mapped_column(primary_key=True)
	children: Mapped[List["Child"]] = relationship(back_populates="parent")


class Child(Base):
	__tablename__ = "child_table"

	id: Mapped[int] = mapped_column(primary_key=True)
	parent_id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"))
	parent: Mapped["Parent"] = relationship(back_populates="children")


Base.metadata.create_all(engine)
