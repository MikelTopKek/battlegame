import storage
from baseunit import BaseUnit


class Unit(BaseUnit):
    """Dummy class. Should be empty"""

    def attack(self, *args, **kwargs):
        pass


class BattleUnit(Unit):
    health_points: int
    damage: int

    def __init__(self, index: int, squad_index: int = None):
        super(BattleUnit, self).__init__(index)

        self.squad_index = squad_index

    def attack(self, enemy):
        health_points = enemy.health_points - self.damage

        new_status_enemy = "DEAD" if health_points <= 0 else None

        storage.Storage.update_human(enemy.index, health_points, new_status_enemy)


class SquadUnit(Unit):
    army_index: int = None
    squad_status = None

    def attack(self, enemy_squad_index):
        pass
