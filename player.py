from entity import Entity


class Player(Entity):
    def __init__(self, name, maxhp=10, damage=3):
        super(Player, self).__init__(name, maxhp, damage)
