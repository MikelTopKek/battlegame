from math import ceil

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

        humans = Storage.get_free_humans(self.index)

        tanks = Storage.get_free_tanks(self.index)

        number_of_human_squads = ceil(self.human_count / self.human_per_squad)
        number_of_tank_squads = ceil(self.tank_count / self.tank_per_squad)

        for i in range(number_of_human_squads):
            human_pack = humans[i * self.human_per_squad: (i + 1) * self.human_per_squad]
            human_pack_indexes = [human.index for human in human_pack]
            squad_index = Storage.add_human_squad(self.index)
            Storage.set_squad_to_humans(
                squad_index=squad_index,
                human_pack_indexes=human_pack_indexes
            )

        for i in range(number_of_tank_squads):
            tank_pack = tanks[i * self.tank_per_squad:(i + 1) * self.tank_per_squad]
            Storage.add_tank_squad(tank_pack)

    def attack(self, *args, **kwargs):
        pass
