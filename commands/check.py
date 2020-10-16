from command import Command, arguments
from commands.command_return_flag import CommandReturnFlag
from command_util import *


def action(game, inputstring):
    args = arguments(inputstring)

    if len(args) == 0:
        target = game.player
    else:
        target = find_target(args[0], game)

    if target is not None:
        print(f"{target.name} has {target.hp}HP and deals {target.damage} damage.")
    else:
        print(f"Invalid target '{args[0]}'!")

    return [CommandReturnFlag.SKIP_EVERYTHING]


class Check(Command):
    def __init__(self):
        super(Check, self).__init__("check", action)
