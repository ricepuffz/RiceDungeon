from command import Command, arguments
from commands.command_return_flag import CommandReturnFlag


def action(game, inputstring):
    args = arguments(inputstring)
    if len(args) == 0:
        if game.current_encounter is not None:
            print(f"You are in an encounter!\n"
                  f"You have {game.player.hp}HP and deal {game.player.damage} damage\n"
                  f"You are fighting against:")
            for enemy in game.current_encounter.enemies:
                print(f"{enemy.name}, who has {enemy.hp}HP and deals {enemy.damage} damage")
    return [CommandReturnFlag.SKIP_EVERYTHING]


class Look(Command):
    def __init__(self):
        super(Look, self).__init__("look", action)
