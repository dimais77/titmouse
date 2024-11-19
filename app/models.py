from typing import Optional
import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class User(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    first_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    second_name: so.Mapped[str] = so.mapped_column(sa.String(64))
    age: so.Mapped[int] = so.mapped_column(sa.Integer)
    parent: so.Mapped[str] = so.mapped_column(sa.String(64))
    phone_number: so.Mapped[str] = so.mapped_column(sa.String(64))
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))


def __repr__(self):
    return "<User {}>".format(self.username)
