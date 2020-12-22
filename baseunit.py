from abc import ABC, abstractmethod
from units import *
from squads import *


# Abstract Factory
class BaseUnit(ABC):

    # def __init__(self):
    #     self.status = None
    #     self.index = None

    @abstractmethod
    def create_human_unit(self) -> Human:
        pass

    @abstractmethod
    def create_human_squad(self) -> HumanSquad:
        pass

    @abstractmethod
    def create_tank_unit(self) -> Tank:
        pass

    @abstractmethod
    def create_tank_squad(self) -> TankSquad:
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