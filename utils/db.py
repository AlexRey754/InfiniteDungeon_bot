from models import *

def init_db():
    with db:
        db.create_tables([Player, Inventory, Achievement, Equipment])

def add_player(uid,name):
    with db:
        querry = Player(uid=uid, name=name, curr_hp=100, max_hp=100,
                        money=0, lvl=1, sp=0, current_xp=0, max_xp=100).save()

def add_money(uid,count):
    with db:
        curr_money = Player.get(Player.uid==uid,Player.money)
        end_money = curr_money + count
        querry = Player(money=end_money).where(Player.uid==uid).update()

def inv_add(uid,item):
    with db:
        querry = Inventory(item==item).where(Inventory.uid==uid).save()