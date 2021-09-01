import random


class Enemy:
    def __init__(self,name,hp,min_dmg,max_dmg,deffence,item,drop_chance) -> None:
        self.name = name
        self.hp = hp
        self.dmg = random.randint(min_dmg, max_dmg+1)
        self.deffence = deffence
        self.item = iitem
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
    def __init__(self, name, description, reward) -> None:
        self.name = name
        self.description = description
        self.reward = reward

    def get(self,uid):
        pass


