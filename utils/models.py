
from peewee import *

db = SqliteDatabase('db.db')

class BaseModel(Model):
    id = PrimaryKeyField(unique=True)
    uid = IntegerField()

    class Meta:
        database = db
        order_by = 'id'


class Player(BaseModel):
    
    name = CharField()
    curr_hp = IntegerField()
    max_hp = IntegerField()
    lvl = IntegerField()
    money = IntegerField()
    sp = IntegerField()
    current_xp = IntegerField()
    max_xp = IntegerField()


class Inventory(BaseModel):

    item = CharField()
    count = CharField()
    

class Achievement(BaseModel):

    name = CharField()


class Equipment(BaseModel):

    head = CharField()
    chest = CharField()
    legs = CharField()
    hand = CharField()


class Stats(BaseModel):

    min_dmg = IntegerField()
    max_dmg = IntegerField()
    deffence = IntegerField