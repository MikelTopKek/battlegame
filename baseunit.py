from abc import ABC, abstractmethod


# Abstract Factory
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


# Concrete Factory1
class BattleUnit(BaseUnit):
    health_points: int
    damage: int

    def __init__(self, index: int, squad_index: int = None):
        super(BattleUnit, self).__init__(index)

        self.squad_index = squad_index

    def attack(self, index, class_type):
        # TODO:::implement feature
        pass


# Concrete Factory2
class SquadUnit(BaseUnit):
    army_index: int

    def __init__(self, index: int, army_index: int):
        super(SquadUnit, self).__init__(index)

        self.army_index = army_index

    def attack(self, index, class_type):
        # TODO:::implement feature
        pass
