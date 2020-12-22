import random

from baseunit import BattleUnit


# Abstract product 1.1
class Human(BattleUnit):
    health_points = 100
    damage = random.randint(30, 50)


human1 = Human(
    index=1,
    squad_index=None
)

# Abstract product 1.2
class Tank:
    pass


# Concrete product 1.1
class Humans(Human):

    def func_humans_human(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"


# Concrete product 1.2
class Tanks(Tank):

    def func_tanks_tank(self) -> str:
        return "product Humans from Human concrete factory Unit factory BaseUnit"




