from command import Command, arguments
from commands.command_return_flag import CommandReturnFlag
from command_util import *


def action(game, inputstring):
    args = arguments(inputstring)

    if len(args) < 1:
        print("You need to specify who you want to attack!")
        return [CommandReturnFlag.SKIP_EVERYTHING]

    target = find_target(args[0], game)
    if target is None:
        print(f"Invalid attack target '{args[0]}'!")
        return [CommandReturnFlag.SKIP_EVERYTHING]

    target.hp -= game.player.damage
    print(f"{game.player.name} attacked {target.name} for {game.player.damage}HP!")
    if target.hp < 1 and target != game.player:
        game.current_encounter.remove_enemy(target)
        print(f"Enemy {target.name} died!")


class Attack(Command):
    def __init__(self):
        super(Attack, self).__init__("attack", action)
