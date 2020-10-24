from item.weapon.crude_bronze_shortsword import CrudeBronzeShortsword


class ItemRegistry:
    game = None
    items = []

    def __init__(self, game):
        self.game = game
        self.register_standard_items()

    def register_item(self, item):
        item.game = self.game
        self.items.append(item)

    def get_item(self, name):
        for item in self.items:
            if item.name == name or item.display_name.lower() == name.lower():
                return item
        return None

    def register_standard_items(self):
        self.register_item(CrudeBronzeShortsword())
