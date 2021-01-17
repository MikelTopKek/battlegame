import army
import countries
import human_tank_and_their_squads
from data import WarStatuses, TypeOfUnit
from random import randint, seed


class Storage:
    armies: list = list()
    list_of_units = list()
    list_of_squads = list()
    countries = list()

    _current_unit_index = 0
    _current_squad_index = 0
    _current_army_index = 0

    @classmethod
    def add_country(cls, name, index, human_count, tank_count, tank_per_squad, human_per_squad,
                    human_squads_per_army, tank_squads_per_army):
        cls.countries.append(countries.Country(name, index, human_count, tank_count, tank_per_squad, human_per_squad,
                                               human_squads_per_army, tank_squads_per_army))

    @classmethod
    def add_humans(cls, number_of_humans) -> list:

        for _ in range(number_of_humans):
            cls.list_of_units.append(
                human_tank_and_their_squads.Human(
                    cls._current_unit_index,
                )
            )
            cls._current_unit_index += 1
        return cls.list_of_units[-number_of_humans:]

    @classmethod
    def add_tanks(cls, number_of_tanks) -> list:
        for _ in range(number_of_tanks):
            cls.list_of_units.append(
                human_tank_and_their_squads.Tank(
                    cls._current_unit_index,
                )
            )
            cls._current_unit_index += 1
        return cls.list_of_units[-number_of_tanks:]

    @classmethod
    def add_human_squad(cls, human_pack_indexes):
        cls.list_of_squads.append(
            human_tank_and_their_squads.HumanSquad(
                index=cls._current_squad_index,
            )
        )
        cls.set_squad_to_humans(
            squad_index=cls._current_squad_index,
            human_pack_indexes=human_pack_indexes
        )
        cls._current_squad_index += 1
        return cls._current_squad_index - 1

    @classmethod
    def add_tank_squad(cls, tank_pack_indexes):
        cls.list_of_squads.append(
            human_tank_and_their_squads.TanksSquad(
                index=cls._current_squad_index,
            )
        )
        cls.set_squad_to_tanks(
            squad_index=cls._current_squad_index,
            tank_pack_indexes=tank_pack_indexes
        )
        cls._current_squad_index += 1

        return cls._current_squad_index - 1

    @classmethod
    def add_army(cls, country_index, human_squads_pack_indexes, tank_squads_pack_indexes) -> int:
        cls.armies.append(
            army.Army(index=cls._current_army_index, country_index=country_index)
        )
        cls.set_army_to_squad(
            army_index=cls._current_army_index,
            human_squads_pack_indexes=human_squads_pack_indexes,
            tank_squads_pack_indexes=tank_squads_pack_indexes
        )
        cls._current_army_index += 1
        return cls._current_army_index

    @classmethod
    def set_squad_to_humans(cls, squad_index, human_pack_indexes):
        for human in cls.list_of_units:
            if human.index in human_pack_indexes:
                human.squad_index = squad_index

    @classmethod
    def set_squad_to_tanks(cls, squad_index, tank_pack_indexes):
        for tank in cls.list_of_units:
            if tank.index in tank_pack_indexes:
                tank.squad_index = squad_index

    @classmethod
    def set_army_to_squad(cls, army_index, human_squads_pack_indexes, tank_squads_pack_indexes):
        for human_squad in cls.list_of_squads:
            if human_squad.index in human_squads_pack_indexes:
                human_squad.army_index = army_index

        for tank_squad in cls.list_of_squads:
            if tank_squad.index in tank_squads_pack_indexes:
                tank_squad.army_index = army_index

    @classmethod
    def update_unit(cls, unit):
        cls.list_of_units[unit.index].health_points = unit.health_points
        cls.list_of_units[unit.index].status = unit.status

    @classmethod
    def fill_squad(cls, squad_index):
        squad_units = list()
        for unit in cls.list_of_units:
            if unit.squad_index == squad_index and unit.status is WarStatuses.STATUS_ALIVE:
                squad_units.append(unit)
        return squad_units

    @classmethod
    def find_free_unit_in_squad(cls, squad_units):
        number_of_units = len(squad_units)
        if number_of_units == 0:
            return WarStatuses.STATUS_DEAD
        seed()
        while True:
            i = randint(0, number_of_units-1)
            if squad_units[i].status is WarStatuses.STATUS_ALIVE:
                break
        return squad_units[i]

    @classmethod
    def squad_status(cls, squad):
        if len(squad) == 0:
            return WarStatuses.STATUS_DEAD
        return WarStatuses.STATUS_ALIVE

    @classmethod
    def find_free_squad_in_army(cls, army_squads):
        number_of_squads = len(army_squads)
        seed()
        if number_of_squads == 0:
            return WarStatuses.STATUS_DEAD
        while True:
            i = randint(0, number_of_squads-1)
            if army_squads[i].status is WarStatuses.STATUS_ALIVE:
                break
        return army_squads[i]

    @classmethod
    def get_army_storage(cls, my_army_index):
        storage = list()
        for squad in Storage.list_of_squads:
            if squad.army_index == my_army_index:
                storage.append(squad)

        for squad in Storage.list_of_squads:
            if squad.army_index == my_army_index:
                storage.append(squad)
        return storage


