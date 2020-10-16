class Entity:
    def __init__(self, name, maxhp=1, damage=1):
        self.name = name
        self.maxhp = maxhp
        self.hp = maxhp
        self.damage = damage
