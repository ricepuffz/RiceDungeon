from item.weapon.weapon import Weapon


class CrudeBronzeShortsword(Weapon):
    def __init__(self):
        super(CrudeBronzeShortsword, self).__init__("crude_bronze_shortsword", "Crude Bronze Shortsword",
                                                    "A very crude and used bronze shortsword, it's a wonder that it "
                                                    "hasn't fallen apart yet..", 4, "1d3")
