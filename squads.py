from baseunit import *
from abc import ABC, abstractmethod


# Abstract product 2.1
class HumanSquad(ABC):

    @abstractmethod
    def abs_func_abstract_squad_human(self) -> str:
        pass


# Abstract product 2.2
class TankSquad(ABC):

    @abstractmethod
    def abs_func_abstract_squad_tank(self) -> str:
        pass


# Concrete product 2.1
class HumansSquad(HumanSquad):

    def func_humans_squad_human_squad(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"


# Concrete product 2.2
class TanksSquad(TankSquad):

    def func_tanks_squad_tank_squad(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"


