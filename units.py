from baseunit import *

# Abstract product 1.1
class Human(ABC):

    @abstractmethod
    def abs_func_abstract_unit_human(self) -> str:
        pass


# Abstract product 1.2
class Tank(ABC):

    @abstractmethod
    def abs_func_abstract_unit_tank(self) -> str:
        pass


# Concrete product 1.1
class Humans(Human):

    def func_humans_human(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"


# Concrete product 1.2
class Tanks(Tank):

    def func_tanks_tank(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"




