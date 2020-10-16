def find_target(name, game):
    name = name.lower()
    if name == "self" or game.player.name.lower() == name:
        return game.player
    if game.current_encounter is not None:
        for enemy in game.current_encounter.enemies:
            if enemy.name.lower() == name:
                return enemy
