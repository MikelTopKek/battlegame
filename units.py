import random

import unit


class Human(unit.BattleUnit):

    def __init__(self, *args, **kwargs):
        super(Human, self).__init__(*args, **kwargs)
        self.health_points = random.randint(100, 100)
        self.damage = random.randint(40, 70)

    def __str__(self):
        return f'<Human[{self.index}]: ' \
               f'hp -> {self.health_points}; ' \
               f'dmg -> {self.damage};' \
               f'status -> {self.status};' \
               f'squad_index -> {self.squad_index}>'


class Tank(unit.BattleUnit):
    health_points = 400

    def __init__(self, *args, **kwargs):
        super(Tank, self).__init__(*args, **kwargs)
        self.damage = random.randint(100, 190)

    def __str__(self):
        return f'<Tank[{self.index}]:' \
               f'hp -> {self.health_points};' \
               f'dmg -> {self.damage};' \
               f'status -> {self.status};' \
               f'squad_index -> {self.squad_index}>'


class TanksSquad(unit.SquadUnit):
    # get_storage_status = ""

    def __str__(self):
        return f'<Tank squad index: {self.index}; ' \
               f'Army index: {self.army_index}>'


class HumanSquad(unit.SquadUnit):
    # get_storage_status = "human_squad_status"

    def __str__(self):
        return f'<Human squad index: {self.index}; ' \
               f'Army index: {self.army_index}>'
