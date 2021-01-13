from enum import Enum

import army
import countries
import units


class WarStatuses(Enum):
    ALIVE = 0
    DEAD = 0


class Storage:
    armies: list = list()
    humans = list()
    tanks = list()
    human_squads = list()
    tank_squads = list()
    countries = list()

    _current_human_index = 0
    _current_human_squad_index = 0

    _current_army_index = 0

    _current_tank_index = 0
    _current_tank_squad_index = 0

    @classmethod
    def add_country(cls, name, index, human_count, tank_count, tank_per_squad, human_per_squad,
                    human_squads_per_army, tank_squads_per_army):
        cls.countries.append(countries.Country(name, index, human_count, tank_count, tank_per_squad, human_per_squad,
                                               human_squads_per_army, tank_squads_per_army))

    @classmethod
    def add_humans(cls, number_of_humans) -> list:

        for _ in range(number_of_humans):
            cls.humans.append(
                units.Human(
                    cls._current_human_index,
                )
            )
            cls._current_human_index += 1
        return cls.humans[-number_of_humans:]

    @classmethod
    def add_tanks(cls, number_of_tanks) -> list:
        for _ in range(number_of_tanks):
            cls.tanks.append(
                units.Tank(
                    cls._current_tank_index,
                )
            )
            cls._current_tank_index += 1
        return cls.tanks[-number_of_tanks:]

    @classmethod
    def add_human_squad(cls, human_pack_indexes):
        cls.human_squads.append(
            units.HumanSquad(
                index=cls._current_human_squad_index,
            )
        )
        cls.set_squad_to_humans(
            squad_index=cls._current_human_squad_index,
            human_pack_indexes=human_pack_indexes
        )
        cls._current_human_squad_index += 1
        return cls._current_human_squad_index - 1

    @classmethod
    def add_tank_squad(cls, tank_pack_indexes):
        cls.tank_squads.append(
            units.TanksSquad(
                index=cls._current_tank_squad_index,
            )
        )
        cls.set_squad_to_tanks(
            squad_index=cls._current_tank_squad_index,
            tank_pack_indexes=tank_pack_indexes
        )
        cls._current_tank_squad_index += 1

        return cls._current_tank_squad_index - 1

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
        for human in cls.humans:
            if human.index in human_pack_indexes:
                human.squad_index = squad_index

    @classmethod
    def set_squad_to_tanks(cls, squad_index, tank_pack_indexes):
        for tank in cls.tanks:
            if tank.index in tank_pack_indexes:
                tank.squad_index = squad_index

    @classmethod
    def set_army_to_squad(cls, army_index, human_squads_pack_indexes, tank_squads_pack_indexes):
        for human_squad in cls.human_squads:
            if human_squad.index in human_squads_pack_indexes:
                human_squad.army_index = army_index

        for tank_squad in cls.tank_squads:
            if tank_squad.index in tank_squads_pack_indexes:
                tank_squad.army_index = army_index

    @classmethod
    def update_human(cls, human_index, human_hp, human_status):

        for human in cls.humans:
            if human.index == human_index:
                human.health_points = human_hp
                if human_status:
                    human.status = human_status

    @classmethod
    def find_free_human_in_squad(cls, squad_index):

        pass

