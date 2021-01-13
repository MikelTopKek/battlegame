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

    def attack(self, enemy2):
        self.health_points -= enemy2.damage
        enemy2.health_points -= self.damage
        if self.health_points <= 0:
            self.status = "DEAD"
        if enemy2.health_points <= 0:
            enemy2.status = "DEAD"
        return self, enemy2


class SquadUnit(Unit):
    army_index: int = None
    squad_status = None

    def attack(self, enemy_squad_index, humans):
        self_minion_index: int = 0
        enemy_minion_index: int = 0
        for human in humans:
            if human.status != "DEAD":
                if human.squad_index == self.index:
                    self_minion_index = human.index
                if human.squad_index == enemy_squad_index:
                    enemy_minion_index = human.index

        self_minion = humans[self_minion_index]
        enemy_minion = humans[enemy_minion_index]
        BattleUnit.attack(self_minion, enemy_minion)
        humans[self_minion_index] = self_minion
        humans[enemy_minion_index] = enemy_minion
        print(self.index, ' ', enemy_minion_index)
        return humans
