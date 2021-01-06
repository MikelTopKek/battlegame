from baseunit import BaseUnit
from storage import Storage


class Country(BaseUnit):

    def __init__(self, name, index, human_count, tank_count, tank_per_squad, human_per_squad):
        super().__init__(index)
        self.name = name
        self.human_count = human_count
        self.tank_count = tank_count
        self.tank_per_squad = tank_per_squad
        self.human_per_squad = human_per_squad
        self.list_of_humans = []

    def __str__(self):
        return f'<Country [{self.index}]: ' \
               f'Human count -> {self.human_count}; ' \
               f'Tank count -> {self.tank_count}...>'

    def generate_units(self):
        Storage.add_humans(self.human_count, self.index)
        Storage.add_tanks(self.tank_count, self.index)

        human_indexes = Storage.get_free_humans(self.index)

        tank_indexes = Storage.get_free_tanks(self.index)

    def attack(self, *args, **kwargs):
        pass
