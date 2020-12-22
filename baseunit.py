from abc import ABC, abstractmethod
from units import *
from squads import *


# Abstract Factory
class BaseUnit(ABC):
    status: int
    index: int

    def __init__(self, index):
        self.index = index

    @abstractmethod
    def attack(self):
        pass


# Concrete Factory1
class BattleUnit(BaseUnit):

    # def __init__(self):
    #     self.damage = None
    #     self.healthPoints = None
    #     self.squadIndex = None

    def attack(self, country_index):
        pass

    def create_human(self) -> Human:
        return Humans()

    def create_tank(self) -> Tank:
        return Tanks()


# Concrete Factory2
class SquadUnit(BattleUnit):

    # def __init__(self):
    #     self.armyIndex = None
    #     self.unitType = None

    def create_squad_human(self) -> HumanSquad:
        return HumansSquad

    def create_squad_tank(self) -> TankSquad:
        return TanksSquad