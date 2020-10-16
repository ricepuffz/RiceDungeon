from entity import Entity


class Enemy(Entity):
    def __init__(self, name, maxhp=5, damage=2):
        super(Enemy, self).__init__(name, maxhp, damage)
