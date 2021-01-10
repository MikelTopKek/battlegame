from math import ceil

from baseunit import BaseUnit
from storage import Storage


def _generate_battle_unit(
        unit_count: int, units_per_squad: int, unit_create: callable,
        unit_create_squad: callable):
    units = unit_create(unit_count)

    number_of_tank_squads = ceil(unit_count / units_per_squad)
    squads_pack_indexes = list()

    for i in range(number_of_tank_squads):
        pack = units[i * units_per_squad: (i + 1) * units_per_squad]
        pack_indexes = [unit.index for unit in pack]
        squad_index = unit_create_squad(pack_indexes)
        squads_pack_indexes.append(squad_index)

    return squads_pack_indexes


class Country(BaseUnit):

    def __init__(self, name, index, human_count, tank_count, tank_per_squad, human_per_squad,
                 human_squads_per_army, tank_squads_per_army):
        super().__init__(index)

        self.name = name
        self.human_count = human_count
        self.tank_count = tank_count
        self.tank_per_squad = tank_per_squad
        self.human_per_squad = human_per_squad
        self.list_of_humans = []
        self.human_squads_per_army = human_squads_per_army
        self.tank_squads_per_army = tank_squads_per_army

        self.generate_units()

    def __str__(self):
        return f'<Country [{self.index}]: ' \
               f'Human count -> {self.human_count}; ' \
               f'Tank count -> {self.tank_count}...>'

    def generate_units(self):
        human_squads_pack_indexes = _generate_battle_unit(
            unit_count=self.human_count,
            units_per_squad=self.human_per_squad,
            unit_create=Storage.add_humans,
            unit_create_squad=Storage.add_human_squad
        )
        tank_squads_pack_indexes = _generate_battle_unit(
            unit_count=self.tank_count,
            units_per_squad=self.tank_per_squad,
            unit_create=Storage.add_tanks,
            unit_create_squad=Storage.add_tank_squad
        )

        number_of_human_squads = len(human_squads_pack_indexes)
        number_of_tank_squads = len(tank_squads_pack_indexes)

        # army generation
        number_of_armies = int(max(number_of_human_squads / self.human_squads_per_army,
                                   number_of_tank_squads / self.tank_squads_per_army))

        print(f'number_of_armies: {number_of_armies} \n'
              f'number_of_human_squads: {number_of_human_squads} \n'
              f'human_squads_per_army: {self.human_squads_per_army} \n'
              f'number_of_tank_squads: {number_of_tank_squads} \n'
              f'tank_squads_per_army: {self.tank_squads_per_army} \n')

        for i in range(number_of_armies):
            pack_index_start = i * self.human_squads_per_army
            pack_indexes_end = (i + 1) * self.human_squads_per_army
            human_squads_pack_indexes_cut = human_squads_pack_indexes[pack_index_start: pack_indexes_end]
            tank_squads_pack_indexes_cut = tank_squads_pack_indexes[pack_index_start: pack_indexes_end]
            Storage.add_army(
                country_index=self.index,
                human_squads_pack_indexes=human_squads_pack_indexes_cut,
                tank_squads_pack_indexes=tank_squads_pack_indexes_cut
            )

    def attack(self, *args, **kwargs):
        pass
