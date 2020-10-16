from command import Command
from commands.command_return_flag import CommandReturnFlag


def action(game, inputstring):
    game.gamerunning = False
    return [CommandReturnFlag.SKIP_EVERYTHING]


class Quit(Command):
    def __init__(self):
        super(Quit, self).__init__("quit", action)
