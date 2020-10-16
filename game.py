from player import Player
from enemy import Enemy
from encounter import Encounter
from command_registry import CommandRegistry
from commands.command_return_flag import CommandReturnFlag


def print_player_death_message():
    print("Welp, you died. Better luck next time!")


class Game:
    command_return_flags = []
    gamerunning = True
    command_registry = None
    player = None
    current_encounter = None

    def __init__(self):
        self.command_registry = CommandRegistry(self)
        self.player = Player("AAAAA")
        enemy = Enemy("Dummy")
        self.current_encounter = Encounter(enemy)
        self.gameloop()

    def gameloop(self):
        while self.gamerunning:
            if self.check_player_dead():
                print_player_death_message()
                return

            # Get player command input
            inputstring = input("\nWhat do you do?: ")
            command = self.command_registry.get_command(inputstring.split(" ")[0])

            # Check if command can be used
            if command is not None and\
                    ((self.current_encounter is None and command.can_be_used_outside_encounter) or
                     (self.current_encounter is not None and command.can_be_used_during_encounter)):
                flags = command.action(self, inputstring)
                self.add_command_return_flags(flags)
            else:
                print(f"\nInvalid command '{inputstring.split(' ')[0]}'!\n"
                      f"Type 'help' for a list of all available commands.")
                self.add_command_return_flag(CommandReturnFlag.SKIP_EVERYTHING)

            if self.check_player_dead():
                print_player_death_message()
                return

            # Let enemies act if there is an encounter
            if not self.check_command_return_flag(CommandReturnFlag.SKIP_EVERYTHING):
                if self.current_encounter is not None:
                    self.current_encounter.enemies_act(self)
                    if len(self.current_encounter.enemies) == 0:
                        print("You won the encounter!")
                        self.current_encounter = None

                if self.check_player_dead():
                    print_player_death_message()
                    return

            self.clear_command_return_flags()

    def check_player_dead(self) -> bool:
        # Check if player is dead
        if self.player.hp < 1:
            self.gamerunning = False
            return True
        return False

    # Command return flag methods
    def add_command_return_flag(self, flag):
        if not self.command_return_flags.__contains__(flag):
            self.command_return_flags.append(flag)

    def add_command_return_flags(self, flags):
        if flags is not None:
            for flag in flags:
                self.add_command_return_flag(flag)

    def remove_command_return_flag(self, flag):
        if self.command_return_flags.__contains__(flag):
            self.command_return_flags.remove(flag)

    def check_command_return_flag(self, flag):
        return self.command_return_flags.__contains__(flag)

    def clear_command_return_flags(self):
        self.command_return_flags = []
