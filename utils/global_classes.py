class Player:
    def __init__(self,name) -> None:
        self.name = name
    
    def add(self,uid,name):
        pass

    def has(self, uid, item, table):
        pass

    def open_characteristics(self,uid):
        pass

    def level_up(self,uid):
        pass

    def get_damaged(self,enemy,uid):
        pass

    def get_xp(self):
        pass

    def equip(self,item,uid):
        pass

    def unequip(self, item, uid):
        pass

    def open_inventory(self, uid):
        pass

    def get_item(self,item,uid):
        pass

    def get_debuff(self,uid):
        pass

    def add_to_inv(self,uid):
        pass

    def add_rand_item_to_inv(self,item_pool,uid):
        pass

    def get_money(self,count,uid):
        pass

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


