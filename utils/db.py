from models import *

def init_db():
    with db:
        db.create_tables([Player, Inventory, Achievement, Equipment])

def add_player(uid,name):
    with db:
        querry = Player(uid=uid,name=name,lvl=1,sp=0,current_xp=0,max_xp=100).save()