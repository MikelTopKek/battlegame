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
        enemy.health_points -= self.damage
        self.health_points -= enemy.damage
        if enemy.health_points < 0:
            enemy.status = "DEAD"
        return enemy


class SquadUnit(Unit):
    army_index: int = None

    def attack(self, enemy_squad):
        pass
