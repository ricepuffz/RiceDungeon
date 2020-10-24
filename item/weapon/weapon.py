from item.item import Item
import util


class Weapon(Item):
    def __init__(self, name, display_name, description, weight, damage):
        super(Weapon, self).__init__(name, display_name, description, weight)
        self.damage = damage

    def roll_damage(self):
        util.parse_damage_string(self.damage)
