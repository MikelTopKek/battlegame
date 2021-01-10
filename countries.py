from math import ceil

from baseunit import BaseUnit
from storage import Storage


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

        human_squads_pack_indexes = list()

        for i in range(number_of_human_squads):
            human_pack = humans[i * self.human_per_squad: (i + 1) * self.human_per_squad]
            human_pack_indexes = [human.index for human in human_pack]
            squad_index = Storage.add_human_squad(self.index)
            human_squads_pack_indexes.append(squad_index)
            Storage.set_squad_to_humans(
                squad_index=squad_index,
                human_pack_indexes=human_pack_indexes
            )

        for i in range(number_of_tank_squads):
            tank_pack = tanks[i * self.tank_per_squad:(i + 1) * self.tank_per_squad]
            tank_pack_indexes = [tank.index for tank in tank_pack]
            squad_index = Storage.add_tank_squad(self.index)
            Storage.set_squad_to_tanks(
                squad_index=squad_index,
                tank_pack_indexes=tank_pack_indexes
            )

        # Lets make armies

        number_of_armies = int(max(number_of_human_squads/self.human_squads_per_army,
                               number_of_tank_squads/self.tank_squads_per_army))
        print(f'number_of_armies: {number_of_armies} \n'
              f'number_of_human_squads: {number_of_human_squads} \n'
              f'human_squads_per_army: {self.human_squads_per_army} \n'
              f'number_of_tank_squads: {number_of_tank_squads} \n'
              f'tank_squads_per_army: {self.tank_squads_per_army} \n')
        for i in range(number_of_armies):
            army_index = Storage.add_army(self.index)
            print('цикл повторился\n')
            human_squads_pack_indexes_cut = human_squads_pack_indexes[i*self.human_squads_per_army:
                                                                      (i+1*self.human_squads_per_army)]
            Storage.set_army_to_squad(
                army_index=army_index,
                human_squads_pack_indexes=human_squads_pack_indexes_cut
            )
            human_squads_pack_indexes = Storage.get_free_human_squads(human_squads_pack_indexes,
                                                                      country_index=self.index)

    def attack(self, *args, **kwargs):
        pass
