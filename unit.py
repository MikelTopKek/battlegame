from baseunit import BaseUnit


class Unit(BaseUnit):

    country_index: int

    def __init__(self, country_index):
        super().__init__(country_index)
        self.country_index = country_index

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
    army_index: int

    def __init__(self, index: int, army_index: int):
        super(SquadUnit, self).__init__(index)

        self.army_index = army_index

    def attack(self, enemy_squad):
        pass