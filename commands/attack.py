from command import Command, arguments
from commands.command_return_flag import CommandReturnFlag
from command_util import *
import util


def action(game, inputstring):
    args = arguments(inputstring)

    if len(args) < 1:
        print("You need to specify who you want to attack!")
        return [CommandReturnFlag.SKIP_EVERYTHING]

    target = find_target(args[0], game)
    if target is None:
        print(f"Invalid attack target '{args[0]}'!")
        return [CommandReturnFlag.SKIP_EVERYTHING]

    dealt_damage = None
    if game.player.equipped_weapon is None:
        dealt_damage = util.parse_damage_string(game.player.damage)
    else:
        dealt_damage = util.parse_damage_string(game.player.equipped_weapon.damage)

    target.hp -= dealt_damage
    print(f"{game.player.name} attacked {target.name} for {dealt_damage}HP!")
    if target.hp < 1 and target != game.player:
        game.current_encounter.remove_enemy(target)
        print(f"Enemy {target.name} died!")


class Attack(Command):
    def __init__(self):
        super(Attack, self).__init__("attack", action)
