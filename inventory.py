import util


class Inventory:
    content = []

    def __init__(self):
        pass

    def add_item(self, item):
        self.content.append(item)

    def remove_item(self, item):
        self.content.remove(item)

    def get_item_from_name(self, name):
        for item in self.content:
            if item.name == name or item.display_name.lower() == name.lower():
                return item
        return None

    def total_weight(self):
        weight = 0
        for item in self.content:
            weight += item.weight
        return weight

    def print_content(self):
        for item in self.content:
            print(item.display_name)
