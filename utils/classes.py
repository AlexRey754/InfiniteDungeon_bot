
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


