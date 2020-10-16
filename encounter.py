class Encounter:
    def __init__(self, *enemies):
        self.enemies = list(enemies)

    def remove_enemy(self, enemy):
        self.enemies.remove(enemy)

    def enemies_act(self, game):
        for enemy in self.enemies:
            game.player.hp -= enemy.damage
            print(f"{enemy.name} attacked {game.player.name} for {enemy.damage}HP!")

            if game.check_player_dead():
                break
