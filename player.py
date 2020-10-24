from entity import Entity


class Player(Entity):
    equipped_weapon = None

    def __init__(self, name, maxhp=10, damage="1d1"):
        super(Player, self).__init__(name, maxhp, damage)

    def equip_weapon(self, weapon):
        if self.equipped_weapon is not None:
            self.inventory.add_item(self.equipped_weapon)
        self.equipped_weapon = weapon
        self.inventory.remove_item(weapon)
