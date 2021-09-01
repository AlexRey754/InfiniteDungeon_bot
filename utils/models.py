from enum import unique
from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db

class Player(BaseModel):
    
    name = CharField()
    lvl = IntegerField()
    skill_points = IntegerField()
    current_xp = IntegerField()
    max_xp = IntegerField()


