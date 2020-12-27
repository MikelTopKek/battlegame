import random

from baseunit import SquadUnit
from storage import Storage


class HumanSquad(SquadUnit):
    health_points = 100

    def __init__(self, *args, **kwargs):
        super(HumanSquad, self).__init__(*args, **kwargs)

        self.damage = random.randint(30, 50)

    def __str__(self):
        return f'<Human[{self.index}]: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'


class TankSquad(SquadUnit):
    health_points = 400

    def __init__(self, *args, **kwargs):
        super(TankSquad, self).__init__(*args, **kwargs)

        self.damage = random.randint(80, 120)

    def __str__(self):
        return f'<Tank[{self.index}: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'
