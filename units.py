import random

from baseunit import BattleUnit
from storage import Storage


class Human(BattleUnit):
    health_points = 100

    def __init__(self, *args, **kwargs):
        super(Human, self).__init__(*args, **kwargs)

        self.damage = random.randint(30, 50)

    def __str__(self):
        return f'<Human[{self.index}]: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'


human1 = Human(
    index=1,
    squad_index=None
)
print(human1)
Storage.humans.append(human1)
Storage.humans.append(
    Human(index=2, squad_index=None)
)
humans = Storage.get_humans_by_squad(squad_index=None)
print(humans)


class Tank(BattleUnit):
    health_points = 400

    def __init__(self, *args, **kwargs):
        super(Tank, self).__init__(*args, **kwargs)

        self.damage = random.randint(80, 120)

    def __str__(self):
        return f'<Tank[{self.index}: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'
