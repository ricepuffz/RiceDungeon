from command import Command
from commands.attack import Attack
from commands.quit import Quit
from commands.check import Check
from commands.look import Look
from commands.help import Help


class CommandRegistry:
    game = None
    commands = []

    def __init__(self, game):
        self.game = game
        self.register_standard_commands()

    def register_command(self, command: Command):
        command.game = self.game
        self.commands.append(command)

    def get_command(self, string):
        for command in self.commands:
            if command.inputstring == string:
                return command
        return None

    def register_standard_commands(self):
        self.register_command(Quit())
        self.register_command(Attack())
        self.register_command(Check())
        self.register_command(Look())
        self.register_command(Help())

        self.commands.sort(key=lambda command: command.inputstring)
