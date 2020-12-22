from abc import ABC, abstractmethod


# Abstract Factory
class BaseUnit(ABC):
    status: int
    index: int

    def __init__(self, index: int):
        self.index = index

    @abstractmethod
    def attack(self, *args, **kwargs):
        pass


# Concrete Factory1
class BattleUnit(BaseUnit):
    health_points: int
    damage: int

    def __init__(self, index: int, squad_index: int):
        super(BattleUnit, self).__init__(index)

        self.squad_index = squad_index

    def attack(self, index, class_type):
        # TODO:::implement feature
        pass


# Concrete Factory2
class SquadUnit(BattleUnit):

    # def __init__(self):
    #     self.armyIndex = None
    #     self.unitType = None

    def create_squad_human(self) -> HumanSquad:
        return HumansSquad

    def create_squad_tank(self) -> TankSquad:
        return TanksSquad