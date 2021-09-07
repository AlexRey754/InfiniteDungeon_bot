import random
from utils.models import *
from entity import player


class Enemy:
    def __init__(self,name,hp,min_dmg,max_dmg,deffence,item,drop_chance) -> None:
        self.name = name
        self.hp = hp
        self.dmg = random.randint(min_dmg, max_dmg+1)
        self.deffence = deffence
        self.item = item
        self.drop_chance = drop_chance

    def drop(self,uid):
        rand = random.randint(0,101)
        if rand <= self.chance:
            db.inv_add(uid=uid,item=self.item)
            return True  # Удача!!!!
        else:
            return False # Ничего не выпало
    

class Item:
    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, min_dmg, max_dmg) -> None:
        super().__init__(name, description)
        self.min_dmg = min_dmg
        self.max_dmg = max_dmg


class Armor(Item):
    def __init__(self, name, description,deffence) -> None:
        super().__init__(name, description)
        self.deffence = deffence


class Achievement:
    def __init__(self, name, description, **kwargs) -> None:
        self.name = name
        self.description = description
        self.reward = kwargs

    def get(self,uid):
        for item,count in self.reward.items():
            if item == 'money':
                player.add_money(uid,count)
            else:
                player.add_to_inv(uid=uid,item=item,count=count)


