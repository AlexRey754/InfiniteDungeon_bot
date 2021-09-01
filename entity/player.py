from utils import db

def add(uid,name):
    db.add_player(uid=uid,name=name)

def has(uid, item, table):
    pass

def open_characteristics(uid):
    pass

def level_up(uid):
    pass

def get_damaged(uid,enemy):
    pass

def get_xp(uid):
    pass

def equip(uid,item):
    pass

def unequip(uid,item):
    pass

def open_inventory(uid):
    pass

def get_item(uid,item):
    pass

def get_debuff(uid):
    pass

def add_to_inv(uid):
    pass

def add_rand_item_to_inv(uid,item_pool):
    pass

def get_money(uid, count):
    db.add_money(uid=uid, count=count)
