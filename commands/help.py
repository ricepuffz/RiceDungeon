from command import Command, arguments
from commands.command_return_flag import CommandReturnFlag


def action(game, inputstring):
    args = arguments(inputstring)

    if len(args) == 0:
        print("All available commands:")
        for command in game.command_registry.commands:
            if (game.current_encounter is not None and command.can_be_used_during_encounter)\
                        or (game.current_encounter is None and command.can_be_used_outside_encounter):
                print(command.inputstring, end="")
                if command.description != "":
                    print(f": {command.description}")
                else:
                    print()

    return [CommandReturnFlag.SKIP_EVERYTHING]


class Help(Command):
    def __init__(self):
        super(Help, self).__init__("help", action, description="Shows a list of all commands or the description of a "
                                                               "specific one")
