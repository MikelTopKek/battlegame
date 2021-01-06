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
    def add_humans(cls, number_of_humans, country_index):
        for _ in range(number_of_humans):
            cls.humans.append(
                Human(
                    cls._current_human_index,
                    country_index
                )
            )
            cls._current_human_index += 1

    @classmethod
    def add_tanks(cls, number_of_tanks, country_index):
        for _ in range(number_of_tanks):
            cls.tanks.append(
                Tank(
                    cls._current_tank_index,
                    country_index
                )
            )
            cls._current_tank_index += 1

    @classmethod
    def get_free_humans(cls, number_of_free_humans, country_index) -> list:
        free_humans = list()
        for _ in range(number_of_free_humans):
            free_humans.append(
                Human(
                    cls._current_human_index,
                    country_index
                )
            )
            cls._current_human_index += 1
        return free_humans

    @classmethod
    def get_free_tanks(cls, number_of_free_tanks, country_index) -> list:
        free_tanks = list()
        for _ in range(number_of_free_tanks):
            free_tanks.append(
                Tank(
                    cls._current_tank_index,
                    country_index
                )
            )
            cls._current_tank_index += 1
        return free_tanks

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
