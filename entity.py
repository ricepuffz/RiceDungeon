from inventory import Inventory


class Entity:
    inventory = None

    def __init__(self, name, maxhp=1, damage=1, weight_capacity=20):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.damage = damage
        self.weight_capacity = weight_capacity

        self.inventory = Inventory()

    def is_encumbered(self):
        return self.inventory.total_weight() > self.weight_capacity
