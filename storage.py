from units import Human, Tank, HumanSquad, TanksSquad


class Storage:
    armies: list = list()
    humans = list()
    tanks = list()
    human_squads = list()
    tank_squads = list()
    countries = list()

    _current_human_index = 0
    _current_human_squad_index = 0

    _current_tank_index = 0
    _current_tank_squad_index = 0

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
    def add_human_squad(cls, human_pack):
        cls.human_squads.append(human_pack)
        cls.set_squad_to_humans(cls._current_human_squad_index)
        cls._current_human_squad_index += 1

    @classmethod
    def add_tank_squad(cls, tank_pack):
        cls.tank_squads.append(tank_pack)
        cls.set_squad_to_tanks(cls._current_tank_squad_index)
        cls._current_tank_squad_index += 1

    # Зачем нужны сет сквады я не понимаю

    @classmethod
    def set_squad_to_humans(cls, squad_index):
        pass

    @classmethod
    def set_squad_to_tanks(cls, human_indexes):
        pass

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
