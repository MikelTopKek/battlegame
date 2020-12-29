from abc import ABC, abstractmethod


class BaseUnit(ABC):
    status: int
    index: int

    def __init__(self, index: int):
        self.index = index

    def __repr__(self):
        return self.__str__()

    @abstractmethod
    def attack(self, *args, **kwargs):
        pass


class BattleUnit(BaseUnit):
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


class SquadUnit(BaseUnit):
    army_index: int

    def __init__(self, index: int, army_index: int):
        super(SquadUnit, self).__init__(index)

        self.army_index = army_index

    def attack(self, enemy_squad):
        pass
