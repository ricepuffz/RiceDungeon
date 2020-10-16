def arguments(string):
    return string.split(" ")[1:]


class Command:
    game = None
    inputstring = None
    action = None
    can_be_used_during_encounter = True
    can_be_used_outside_encounter = True

    def __init__(self, inputstring, action, description=""):
        self.inputstring = inputstring
        self.action = action
        self.description = description
