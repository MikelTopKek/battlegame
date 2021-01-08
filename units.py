import random

from unit import BattleUnit, SquadUnit


class Human(BattleUnit):
    health_points = 100

    def __init__(self, *args, **kwargs):
        super(Human, self).__init__(*args, **kwargs)

        self.damage = random.randint(30, 50)

    def __str__(self):
        return f'<Human[{self.index}]: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'


class Tank(BattleUnit):
    health_points = 400

    def __init__(self, *args, **kwargs):
        super(Tank, self).__init__(*args, **kwargs)

        self.damage = random.randint(80, 120)

    def __str__(self):
        return f'<Tank[{self.index}: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage}>'


class TanksSquad(SquadUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'<TankSquad[{self.index}>'


class HumanSquad(SquadUnit):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def __str__(self):
        return f'<HumanSquad[{self.index}>'
