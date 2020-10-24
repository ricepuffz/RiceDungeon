from command import Command
from commands.command_return_flag import CommandReturnFlag
from inventory import Inventory


def action(game, inputstring):
    game.player.inventory.print_content()
    return [CommandReturnFlag.SKIP_EVERYTHING]


class Inventory(Command):
    def __init__(self):
        super(Inventory, self).__init__("inventory", action)
