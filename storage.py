from units import Human, Tank, HumanSquad, TanksSquad
from army import Army


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
    def add_army(cls, country_index) -> int:
        cls.armies.append(Army(index=cls._current_army_index, country_index=country_index))
        cls._current_army_index += 1
        return cls._current_army_index

    @classmethod
    def add_country(cls, country):
        cls.countries.append(country)

    @classmethod
    def add_humans(cls, number_of_humans, country_index) -> list:
        for _ in range(number_of_humans):
            cls.humans.append(
                Human(
                    cls._current_human_index,
                    country_index
                )
            )
            cls._current_human_index += 1

        return cls.humans[:-number_of_humans]

    @classmethod
    def add_tanks(cls, number_of_tanks, country_index) -> list:
        for _ in range(number_of_tanks):
            cls.tanks.append(
                Tank(
                    cls._current_tank_index,
                    country_index
                )
            )
            cls._current_tank_index += 1

        return cls.tanks[:-number_of_tanks]

    @classmethod
    def add_human_squad(cls, country_index):
        cls.human_squads.append(
            HumanSquad(
                index=cls._current_human_squad_index,
                country_index=country_index,
            )
        )
        cls._current_human_squad_index += 1

        return cls._current_human_squad_index - 1

    @classmethod
    def add_tank_squad(cls, country_index):
        cls.tank_squads.append(
            TanksSquad(
                index=cls._current_tank_squad_index,
                country_index=country_index
            )
        )
        cls._current_tank_squad_index += 1

        return cls._current_tank_squad_index - 1

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
    def get_free_humans(cls, country_index) -> list:

        def filter_rule(human):
            return human.squad_index is None and human.country_index == country_index

        return list(filter(filter_rule, cls.humans))

    @classmethod
    def get_free_tanks(cls, country_index) -> list:

        def filter_rule(tank):
            return tank.squad_index is None and tank.country_index == country_index

        return list(filter(filter_rule, cls.tanks))

    # Get free squads
    @classmethod
    def get_free_human_squads(cls, human_squads_indexes_pack, country_index) -> list:

        humans = cls.humans
        human_squads = cls.human_squads

        def filter_rule1(human_squad_index):
            for human in humans:
                if human.squad_index in human_squads_indexes_pack and human.country_index == country_index:
                    for human_squad in human_squads:
                        if human_squad.index == human_squad_index and human_squad.army_index is None:
                            return True

        # def filter_rule2(human_squads, human):
        #     return human_squads.army_index is None and human in human_squads and filter_rule1(human)

        return list(filter(filter_rule1, human_squads_indexes_pack))

    @classmethod
    def set_army_to_squad(cls, army_index, human_squads_pack_indexes):
        for human_squad in cls.human_squads:
            if human_squad.index in human_squads_pack_indexes:
                human_squad.army_index = army_index

        # for tank_squad in cls.tank_squads:
        #     if tank_squad.index in tank_squads_pack_indexes:
        #         tank_squad.army_index = army_index

    @classmethod
    def get_elem_by_index(cls, index: int, elem_type: str) -> list:
        list_data = ...  # TODO:::this data should depends on the elem_type

        # return list(filter(lambda x: x.index == index, list_data))
        # the same here \/
        def filter_rule(x):
            return x.index == index

        return list(filter(filter_rule, list_data))

    @classmethod
    def get_humans_by_squad(cls, squad_index: int) -> list:
        return list(
            filter(
                lambda x: x.squad_index == squad_index,
                cls.humans
            )
        )
