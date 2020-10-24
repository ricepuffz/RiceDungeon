from command import Command


def action(game, inputstring):
    split = inputstring.split(" ")[1:]
    splitlen = len(split)
    item_name = ""

    for i in range(splitlen):
        item_name += split[i]
        if i != splitlen - 1:
            item_name += " "

    item = game.player.inventory.get_item_from_name(item_name)

    game.player.equip_weapon(item)


class Equip(Command):
    def __init__(self):
        super(Equip, self).__init__("equip", action)
