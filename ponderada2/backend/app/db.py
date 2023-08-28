# app/db.py

import databases
import ormar
import sqlalchemy

#from .config import settings

database = databases.Database(settings.db_url)
#database = databases.Database("sqlite:///db.sqlite3")
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    id: int = ormar.Integer(primary_key=True)
    email: str = ormar.String(max_length=128, unique=True, nullable=False)
    password: str = ormar.String(max_length=128, nullable=False)

class ToDo(ormar.Model):
    class Meta(BaseMeta):
        tablename = "todocard"

    id: int = ormar.Integer(primary_key=True)
    title: str = ormar.String(max_length=128, unique=True, nullable=False)
    content: str = ormar.String(max_length=128, unique=True, nullable=False)
    user_id: int = ormar.Integer()

engine = sqlalchemy.create_engine(settings.db_url)
metadata.create_all(engine)
